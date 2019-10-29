(define (accumulate combiner start n term)
  (if (= n 0)
    start
    (combiner (accumulate combiner
      start
      (- n 1)
      term)
    (term n)))
)

(define (accumulate-tail combiner start n term)
  (if (= n 0)
    start
    (accumulate-tail combiner (combiner (term n) start) (- n 1) term))
)

(define (rle s)
  (define (tracker in out num)
    (cond
      ((null? out) (cons-stream (list in num) nil))
      ((= (car out) in) (tracker in (cdr-stream out) (+ num 1)))
      (else (cons-stream (list in num) (rle out)))
    )
  )

  (if (null? s) nil (tracker (car s) (cdr-stream s) 1))
)
