;linear recursive process 
(define (fact n)
  (if (= n 1)
      1
      (* n (facto (- n 1)))))
;linear iterative process 
(define (fact n)
    (fact-iter 1 1 n))
(define (fact-iter count product n)
    (if (> count n)
        product
        (fact-iter (+ count 1)
                   (* product count)
                   n)))

;exercise-1.9
(define (+ a b)
  (if (= a 0)
      b
      (inc (+ (dec a) b))))
;ans: recursive process. Output is 9

(define (+ a b)
  (if (= a 0)
      b
      (+ (dec a) (inc b))))
;ans: iterative process. Output is 9

;exercise-1.10
(A 1 10) ;1024
(A 2 4) ;65536
(A 3 3) ;65536

(define (f n) (A 0 n)) ;2n
#|
(A 0 n) => (* 2 n)
よって2n
|#

(define (g n) (A 1 n)) ;2^n
#|
(A 1 n) => (A 0 (A 1 (- n 1))) => (f (g (- n 1))) => (f (f (g (- n 1)))) => ... 
(f n) = 2n　よって2 * 2 * ... * 2がn回掛けられる
答えは2^n
|#

(define (h n) (A 2 n)) ;tet(2 n)
#|
(A 2 n) => (A 1 (A 2 (- n 1))) => (g (h (- n 1))) => (g (g (h (- n 2)))) => ...
(g n) = 2^n nが2に代わってn回指数の繰り返しをする。n = 3だとすると(((2^2)^2)^2)
答えはtet(2, n)
|#

;tree recursion for computing fibonacci numbers
(define (fib n)
  (cond ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (fib (- n 1))
                 (fib (- n 2))))))

;linear iteration process 
(define (fib n)
    (define (fib-iter a b count)
        (if (= count 0)
            b
            (fib-iter 
                (+ a b) 
                a 
                (- count 1))))
    (fib-iter 1 0 n))
;tree recursion for  count change
(define (count-change amount)
    (cc amount 5))

(define (cc amount kinds-of-coins)
    (cond ((= amount 0) 1)
          ((or (< amount 0) (= kinds-of-coins 0)) 0)
          (else (+ (cc amount
                     (- kinds-of-coins 1))
                   (cc (- amount
                        (first-denomination kinds-of-coins))
                        kinds-of-coins)))))

(define (first-denomination kinds-of-coins)
    (cond ((= kinds-of-coins 1) 1)
          ((= kinds-of-coins 5) 5)
          ((= kinds-of-coins 10) 10)
          ((= kinds-of-coins 25) 25)
          ((= kinds-of-coins 50) 50)))

;exercise 1.11
;recursive process
(define (f n)
    (if (< n 3)
        n
        (+ (f (- n 1))
           (* 2 (f (- n 2)))
           (* 3 (f (- n 3))))))

;iterative process
(define (f n)
    (define (iter-f a b c n)
            (if (= n 0)
                a
                (iter-f (+ a (* 2 b) (* 3 c))
                        a
                        b
                        (- n 1))))
    (iter-f 2 1 0 n))
|*
a: f(n - 1)
b: f(n - 2)
c: f(n - 3)
*|

;exercise 1.12
#|
depth: a
oreder from left: b
f(a, b) = 1 if a = 1 or b = 1
f(a, b) = f(a-1, b-1) + f(a-1, b)
|#
(def (f a b)
    (if (or (= a 1) (= b a))
        1
        (+ (f (- a 1) (- b 1))
           (f (- a 1) b))))


