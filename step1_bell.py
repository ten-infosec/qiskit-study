# Qiskit 1단계: 두 큐비트를 얽히게 만들고 1000번 측정하기 (벨 상태)


from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

print(qc.draw())

sampler = StatevectorSampler()
result = sampler.run([qc], shots=1000).result()
counts = result[0].data.meas.get_counts()

print("측정 결과:", counts)


# from qiskit import QuantumCircuit → 양자 회로를 만드는 도구를 가져오겠다
# from qiskit.primitives import StatevectorSampler → 내 컴퓨터에서 양자 회로를 흉내 내어 실행하는 시뮬레이터를 가져오겠다
# qc = QuantumCircuit(2) → 큐비트 2개짜리 빈 회로를 만들겠다 (둘 다 0에서 시작)
# qc.h(0) → 0번 큐비트에 H 게이트를 걸어 "0과 1이 반반 섞인 상태"로 만들겠다
# qc.cx(0, 1) → CNOT 게이트: 0번이 1이면 1번을 뒤집어서, 두 큐비트를 얽히게 만들겠다
# qc.measure_all() → 모든 큐비트를 측정하고 결과를 'meas'라는 이름의 칸에 담겠다
# print(qc.draw()) → 회로를 글자 그림으로 터미널에 그려보겠다
# sampler.run([qc], shots=1000) → 이 회로를 1000번 반복 실행하겠다 (shots = 반복 횟수)
# result[0].data.meas.get_counts() → 첫 번째 회로의 측정 결과를 "어떤 결과가 몇 번 나왔는지"로 세겠다