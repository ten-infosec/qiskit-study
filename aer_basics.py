# 회로 만들기 (앨리스가 대각기저로 보내고, 밥이 대각기저로 측정)


from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.barrier()
qc.h(0)
qc.measure(0, 0)
print(qc.draw())


# → QuantumCircuit(1, 1) : 큐비트 1개, 측정값을 적을 고전 비트 1개짜리 회로를 만들겠다
# → qc.h(0) : 앨리스가 0번 큐비트에 H를 걸어 대각기저 상태로 보내겠다
# → qc.barrier() : 앨리스 구역과 밥 구역 사이에 칸막이를 세우겠다
# → qc.h(0) : 밥이 H를 한 번 더 걸어 대각기저로 읽을 준비를 하겠다 (H 두 번 = 원래대로)
# → qc.measure(0, 0) : 0번 큐비트를 측정해서 0번 고전 비트에 적겠다
# → print(qc.draw()) : 회로를 글자 그림으로 터미널에 보여주겠다


# 시뮬레이터로 1024번 실행하고 결과 저장


sim = AerSimulator()
compiled = transpile(qc, sim)
result = sim.run(compiled, shots=1024).result()
counts = result.get_counts()
print("측정 결과:", counts)

fig = plot_histogram(counts)
fig.savefig("aer_basics_hist.png")
print("히스토그램 저장: aer_basics_hist.png")


# → AerSimulator() : 교재의 Aer.get_backend('aer_simulator')를 요즘 방식으로 바꿔 시뮬레이터를 만들겠다
# → transpile(qc, sim) : 회로를 시뮬레이터가 이해하는 게이트로 변환하겠다
# → sim.run(..., shots=1024) : 같은 회로를 1024번 반복 실행하겠다 (shots = 실행 횟수)
# → .result().get_counts() : 결과별로 몇 번 나왔는지 세서 {'0': 1024} 같은 형태로 받겠다
# → plot_histogram(counts) : 결과를 막대그래프로 그리겠다
# → fig.savefig(...) : 스크립트로 실행하면 그림 창이 안 뜨니, 그래프를 PNG 파일로 저장하겠다