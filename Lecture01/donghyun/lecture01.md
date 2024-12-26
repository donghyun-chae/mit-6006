## Asymptotics Exercises

### 1. 10개의 함수를 생성하고 점근적 성장률로 정렬하기

> k < log n < log n < √n < n < n log n < n² < n³ < 2ⁿ < n! < nⁿ

### 2. n개의 항목 중에서 6006개를 선택하는 조합의 점근적 성장률

> 분자: n(n-1)(n-2)...(n-6005) (6006차 다항식)  
> 분모: 6006! (n에 대한 상수)  
> 이기 때문에 분모는 O(1) - 상수시간이기에 분자의 O(n^6006) - 6006차 다항식의 성장률을 따라감

### 3. log₆₀₀₆(log√n²)의 점근적 한계 찾기

> log(a^b) = b log(a), log₂(ab) = log₂(a) + log₂(b), logₐ(b) = log(b)/log(a)  
> 위의 법칙을 사용한 계산 log₆₀₀₆(log√n²) = log(log n)/log(6006) = Θ(log n)

### 4. 2^(n+1)∈Θ(2ⁿ)이지만 2^(2n+1)∉O(2^(2n)) 증명

> a) 2^(n+1) = 2 · 2ⁿ

- 단순히 2ⁿ에 상수 2를 곱한 것
- 따라서 Θ(2ⁿ)에 속함

> b) 2^(2n+1) = 2^(2n) · 2

- 2^(2n)의 제곱
- 상수 배수가 아닌 지수적 차이
- 따라서 O(2^(2n))에 속하지 않음

### 5. 모든 양의 상수 a, b에 대해 (log n)^a = O(n^b) 증명

> 1. n^b/(log n)^a가 n→∞일 때 ∞로 발산함을 보임
> 2. 로그를 취해서 증명:
>    lim(b log n - a log log n) = ∞
>    참고: 같은 이유로 n^a = O(c^n), c > 1

### 6. (log n)^(log n) = Ω(n) 증명

> 1. m = Ω(2^m) 성질 이용
> 2. n = 2^m 대입으로 증명 완성

### 7. (6n)! ∉ Θ(n!)이지만 log((6n)!) ∈ Θ(log(n!)) 증명

> 1. 스털링 근사 사용:
>    n! = √(2πn)(n/e)ⁿ(1 + Θ(1/n))
> 2. (6n)!의 경우:
>
> - 적어도 6^(6n)배 더 큼
> - Θ(n!)에 속할 수 없음
>
> 3.  log 취했을 때:
>     log(n!) = Θ(n log n)
>
> - 6n 대입해도 상수 차이만 발생
> - 따라서 Θ(log(n!))에 속함