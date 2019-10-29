test = {
  'name': 'quasiquote',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> '(1 2 3)
          (1 2 3)
          scm> `(1 2 3)
          (1 2 3)
          scm> `(1 x 3)
          (1 x 3)
          scm> (define x 2)
          x
          scm> `(1 x 3)
          (1 x 3)
          scm> `(1 ,x 3)
          (1 2 3)
          scm> '(1 ,x 3)
          f03c73dfe0ea05607e0335cd06e5f220
          # locked
          scm> `(,1 x 3)
          7026b4496459392f36b9a5b9dc64e31d
          # locked
          scm> `,(1 x 3)
          c6d536c5acab2b28e563f34c64535296
          # locked
          scm> `,(+ 1 x 3)
          71dc1c0558e41b2d6d30fd9795b4fb1f
          # locked
          scm> `(1 (,x) 3)
          d6cbc2f9e22d26450e36a1a1389f6877
          # locked
          scm> `(1 ,(+ x) 3)
          f22d790116f4f90477aa1ae1655e6839
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
