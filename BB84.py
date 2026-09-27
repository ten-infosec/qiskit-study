# BB84 양자 키 분배 시뮬레이션: 도청자 없음 vs 도청자 있음


import random
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

N = 200
random.seed(7)
sampler = StatevectorSampler()


def measure_once(circuits):
    result = sampler.run(circuits, shots=1).result()
    return [int(list(r.data.c.get_counts().keys())[0]) for r in result]


def prepare(bit, basis):
    qc = QuantumCircuit(1, 1)
    if bit == 1:
        qc.x(0)
    if basis == "X":
        qc.h(0)
    return qc


def add_measure(qc, basis):
    if basis == "X":
        qc.h(0)
    qc.measure(0, 0)
    return qc


def run_bb84(with_eve):
    alice_bits = [random.randint(0, 1) for _ in range(N)]
    alice_bases = [random.choice("ZX") for _ in range(N)]
    bob_bases = [random.choice("ZX") for _ in range(N)]

    sent = [(b, s) for b, s in zip(alice_bits, alice_bases)]

    if with_eve:
        eve_bases = [random.choice("ZX") for _ in range(N)]
        eve_circuits = [add_measure(prepare(b, s), e) for (b, s), e in zip(sent, eve_bases)]
        eve_bits = measure_once(eve_circuits)
        sent = list(zip(eve_bits, eve_bases))

    bob_circuits = [add_measure(prepare(b, s), bb) for (b, s), bb in zip(sent, bob_bases)]
    bob_bits = measure_once(bob_circuits)

    keep = [i for i in range(N) if alice_bases[i] == bob_bases[i]]
    alice_key = [alice_bits[i] for i in keep]
    bob_key = [bob_bits[i] for i in keep]

    errors = sum(a != b for a, b in zip(alice_key, bob_key))
    qber = errors / len(keep)
    return alice_key, bob_key, qber


for with_eve in (False, True):
    a_key, b_key, qber = run_bb84(with_eve)
    label = "도청자 있음" if with_eve else "도청자 없음"
    print(f"[{label}]")
    print(f"  보낸 큐비트 {N}개 → 기저가 같아 남긴 비트 {len(a_key)}개")
    print(f"  앨리스 키 앞 20자리: {''.join(map(str, a_key[:20]))}")
    print(f"  밥 키   앞 20자리: {''.join(map(str, b_key[:20]))}")
    print(f"  오류율(QBER): {qber:.1%}")
    print()


# N = 200 → 앨리스가 보낼 큐비트 개수를 200개로 정하겠다
# random.seed(7) → 무작위 값을 매번 똑같이 나오게 고정하겠다 (지우면 매번 달라짐)
# measure_once → 회로 여러 개를 각각 딱 한 번씩 실행해 측정값(0 또는 1)만 뽑겠다
# prepare(bit, basis) → 앨리스가 비트 하나를 안경(Z 또는 X) 하나로 큐비트에 담겠다
# add_measure(qc, basis) → 받는 쪽이 자기 안경으로 큐비트를 읽겠다 (안경이 같으면 원래 값이 나옴)
# run_bb84(with_eve) → 앨리스 전송 → (이브 가로채기) → 밥 측정 → 안경 공개 비교 → 같은 자리만 남기기
# keep → 앨리스와 밥의 안경이 같았던 자리만 고르겠다 (비트 값은 공개하지 않음)
# qber → 오류율 = 두 열쇠에서 서로 다른 비트 수 / 남긴 비트 수
# for with_eve in (False, True) → 도청자 없는 경우와 있는 경우를 차례로 실행하겠다