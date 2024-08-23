; execercise 1.2
(/ (+ 5 4 (- 2 (- 3 (+ 6 (/ 4 5)))))
   (* 3 (- 6 2) (- 2 7)))

; execercise 1.3
(define (<= x y)
  (not (> x y)))
(define (square x)
  (* x x))
(define (sum-of-square x y)
  (+ (square x) (square y)))
(define (choose-bigger2-of-3num a b c)
  (cond ((and (<= a b) (<= a c)) (sum-of-square b c))
        ((and (<= b a) (<= b c)) (sum-of-square a c))
        ((and (<= c a) (<= c b)) (sum-of-square a b))))

; exercise 1.5
(define (abs x)
  (if (> x 0)
    x
    (- x)))
(define (good-enough? guess x)
  (< (abs (- (square guess) x)) 0.001))
(define (average x y)
  (/ (+ x y)
     2))
(define (improve guess x)
  (average guess (/ x guess)))
(define (sqrt-iter guess x)
  (if (good-enough? guess x)
    guess
    (sqrt-iter (improve guess x) x)))
(define (sqrt x)
  (sqrt-iter 1 x))

; execercise 1.6
#|
(define (new-if predicate then-clause else-clause)
  (cond (predicate then-clause)
        (else else-clause)))
(define (sqrt-iter guess x)
  (new-if (good-enough? guess x)
          guess
          (sqrt-iter (improve guess x)
                     x)))
|#

; exercise 1.7
(define (good-enough? guess1 guess2) 
    (< 
      (/ (abs (- guess2 guess1)) guess1)
      0.001))

(define (sqrt-iter guess x)
    (let ((better (improve guess x)))
        (if (good-enough? guess better)
            guess
            (sqrt-iter (improve better x) x))))

(define (sqrt x)
  (sqrt-iter 1 x))

; exercise 1.8
(define (cube x) (* x x x))

(define (good-enough? guess x)
  (< (abs (- (cube guess) x)) 0.001)
  )

(define (improve y x)
  (/ (+ (/ x (square y))
        (* 2 y))
     3))

(define (cube-iter guess x)
    (if (good-enough? guess x)
      guess
      (cube-iter (improve guess x) x)))

(define (cbrt x)
    (cube-iter 1.0 x))

; 1.1.8  Procedures as Black-Box Abstractions
(define (sqrt x)
    (define (good-enough? guess x)
        (< (abs (- (square guess) x)) 0.001))
    (define (improve guess x)
        (average guess (/ x guess)))
    (define (sqrt-iter guess x)
        (if (good-enough? guess x)
          guess
          (sqrt-iter (improve guess x) x)))
    (sqrt-iter 1.0 x)
    )

; x is bound in the sqrt, so also can write block structure such as...
(define (sqrt x)
    (define (good-enough? guess)
        (< (abs (- (square guess) x)) 0.001))
    (define (improve guess)
        (average guess (/ x guess)))
    (define (sqrt-iter guess)
        (if (good-enough? guess)
          guess
          (sqrt-iter (improve guess))))
    (sqrt-iter 1.0)
    )
