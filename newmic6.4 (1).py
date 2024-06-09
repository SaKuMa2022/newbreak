import streamlit as st
import pandas as pd



MIC=[  ['≤ 8 | 16 | ≥ 32', '≤ 8/4 | 16/8 | ≥ 32/16',	'≤ 8/4 | 16/8 | ≥ 32/16','≤ 2/4 | 4/4 | ≥ 8/4',	'≤ 8/4 | 16/4 | ≥ 32/4', '≤ 8/4 | – | ≥ 16/4',	'≤ 4/8 | 8/8 | ≥ 16/8',	'≤ 2 | 4 | ≥ 8', '≤ 16 | – | ≥ 32', '≤ 1 |2 | ≥ 4', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', 
                    '≤ 8 | 16 | ≥ 32', '≤ 2 | 4-8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', 
                        '≤ 2 | 4 | ≥ 8', '≤ 2 | 4 | ≥ 8', 'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.25 | 0.5 | ≥ 1', 
                        '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],

                      [ '≤ 8 | 16 | ≥ 32',	'≤ 8/4 | 16/8 | ≥ 32/16', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 2/4 | 4/4 | ≥ 8/4', '≤ 8/4 | 16/4 | ≥ 32/4', '≤ 8/4 | – | ≥ 16/4', '≤ 4/8 | 8/8 | ≥ 16/8', 
                        '≤ 2 | 4 | ≥ 8', '≤ 16 | – | ≥ 32', '≤ 1 |2 | ≥ 4', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 8 | 16 | ≥ 32', '≤ 2 | 4-8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 
                    '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 2 | 4 | ≥ 8', '≤ 2 | 4 | ≥ 8', 'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 
                    '≤ 0.25 | 0.5 | ≥ 1', '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],

                        ['≤ 8 | 16 | ≥ 32', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 2/4 | 4/4 | ≥ 8/4', '≤ 8/4 | 16/4 | ≥ 32/4',
                        '≤ 8/4 | – | ≥ 16/4', '≤ 4/8 | 8/8 | ≥ 16/8', '≤ 2 | 4 | ≥ 8', '≤ 16 | – | ≥ 32', '≤ 1 |2 | ≥ 4', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 8 | 16 | ≥ 32', 
                        '≤ 2 | 4-8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', 
                    '≤ 2 | 4 | ≥ 8', '≤ 2 | 4 | ≥ 8', 'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.25 | 0.5 | ≥ 1', '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],

                        ['≤ 8 | 16 | ≥ 32', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 2/4 | 4/4 | ≥ 8/4', '≤ 8/4 | 16/4 | ≥ 32/4',
                        '≤ 8/4 | – | ≥ 16/4', '≤ 4/8 | 8/8 | ≥ 16/8', '≤ 2 | 4 | ≥ 8', '≤ 16 | – | ≥ 32', '≤ 1 |2 | ≥ 4', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 8 | 16 | ≥ 32', 
                        '≤ 2 | 4-8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 2 | 4 | ≥ 8', '≤ 2 | 4 | ≥ 8', 
                        'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.25 | 0.5 | ≥ 1', '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],



                     ['≤ 8 | 16 | ≥ 32', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 2/4 | 4/4 | ≥ 8/4', '≤ 8/4 | 16/4 | ≥ 32/4', '≤ 8/4 | – | ≥ 16/4', '≤ 4/8 | 8/8 | ≥ 16/8',
                        '≤ 2 | 4 | ≥ 8', '≤ 16 | – | ≥ 32', '≤ 1 |2 | ≥ 4', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 8 | 16 | ≥ 32', '≤ 2 | 4-8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 
                    '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 2 | 4 | ≥ 8', '≤ 2 | 4 | ≥ 8', 'not reported', 'not reported', 	'≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 
                        '≤ 0.25 | 0.5 | ≥ 1', '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],

                      ['≤ 8 | 16 | ≥ 32', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 2/4 | 4/4 | ≥ 8/4', '≤ 8/4 | 16/4 | ≥ 32/4', '≤ 8/4 | – | ≥ 16/4', '≤ 4/8 | 8/8 | ≥ 16/8', 
                        '≤ 2 | 4 | ≥ 8', '≤ 16 | – | ≥ 32', '≤ 1 |2 | ≥ 4', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 8 | 16 | ≥ 32', '≤ 2 | 4-8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 
                        '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 2 | 4 | ≥ 8', '≤ 2 | 4 | ≥ 8', 'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 
                        '≤ 0.25 | 0.5 | ≥ 1', '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],

                     ['≤ 8 | 16 | ≥ 32', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 2/4 | 4/4 | ≥ 8/4', '≤ 8/4 | 16/4 | ≥ 32/4', '≤ 8/4 | – | ≥ 16/4', '≤ 4/8 | 8/8 | ≥ 16/8', 
                        '≤ 2 | 4 | ≥ 8', '≤ 16 | – | ≥ 32', '≤ 1 |2 | ≥ 4', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 8 | 16 | ≥ 32', '≤ 2 | 4-8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 
                        '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 2 | 4 | ≥ 8', '≤ 2 | 4 | ≥ 8', 'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16',
                        '≤ 0.25 | 0.5 | ≥ 1', '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],

                    ['≤ 8 | 16 | ≥ 32', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', '≤ 1 |2 | ≥ 4', 
                    '≤ 1 |2 | ≥ 4', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', 'not reported', 'not reported', 
                        'not reported', 'S. enterica ser. Typhi only ≤ 16 |– |≥ 32', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.06 | 0.12- 0.5 | ≥ 1', '≤ 0.12 | 0.25- 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],


                      ['≤ 8 | 16 | ≥ 32', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', '≤ 1 |2 | ≥ 4', 
                     '≤ 1 |2 | ≥ 4', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', 'not reported', 'not reported', 
                        'not reported', '≤ 8 | 16 | ≥ 32', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.25 | 0.5 | ≥ 1', '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],



                     ['not reported', 'not reported', 'not reported', '≤ 4/4 | 8/4 | ≥ 16/4', '≤ 16/4 | 32/4 | ≥ 64/4', '≤ 8/4 | – | ≥ 16/4', 'not reported', 'not reported', 
                        'not reported', 'not reported', 'not reported', '≤ 8 | 16 | ≥ 32', 'not reported', '≤ 8 | 16 | ≥ 32', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 8 | 16 | ≥ 32', 'not reported',
                        '≤ 2 | 4 | ≥ 8', '≤ 16 | 32 | ≥ 64', 'not reported', '≤ 1 |2 | ≥ 4', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', 'not reported', 'not reported'],



                     ['not reported', '≤ 8/4 | 16/8 | ≥ 32/16', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 
                        '≤ 8 | 16–32 | ≥ 64', '≤ 8 | 16–32 | ≥ 64', '≤ 8 | 16 | ≥ 32', 'not reported', '≤ 8 | 16 | ≥ 32', 'not reported', '≤ 4 | 8 | ≥ 16', 'not reported', 'not reported', 
                    '≤ 2 | 4 | ≥ 8', '≤ 16 | 32 | ≥ 64', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 1 |2 | ≥ 4', '≤ 2 | 4 | ≥ 8', 'not reported', '≤ 2/38 | – | ≥ 4/76'],


                      ['not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 
                    'not reported', 'not reported', '≤ 8 | 16 | ≥ 32', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', 'not reported', 'not reported', 
                        'not reported', 'not reported', 'not reported', 'not reported', 'not reported', '≤ 4 | 8  | ≥ 16', 'not reported', '≤ 2 | 4 | ≥ 8', 'not reported', '≤ 2/38 | – | ≥ 4/76'],



                     ['not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported',
                        'not reported', 'not reported', 'not reported', 'not reported', 'not reported', '≤ 1', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 
                        'not reported', 'not reported', 'not reported', 'not reported', '≤ 1 | 2 | ≥ 4', 'not reported', '≤ 2 | 4 | ≥ 8', 'not reported', '≤ 2/38 | – | ≥ 4/76'],


                      ['≤ 1  |  2 | ≥ 4', '≤ 2/1 | – | ≥ 4/2', '≤ 2/1 | 4/2 | ≥ 8/4', '≤ 0.5/4', '≤ 1/4 | – | ≥ 2/4', 'not reported', 'not reported', 'not reported', 'not reported', 
                        '≤ 2', '≤ 2', '≤ 2', '≤ 4 | 8 | ≥ 16', '≤ 2', '≤ 0.5', 'not reported', '≤ 2', '≤ 0.5', '≤ 0.5', 'not reported', 'not reported', 'not reported', '≤ 4', '≤ 8 | 16 | ≥ 32', '≤ 2 | 4 | ≥ 8',
                        'not reported', 'not reported', '≤ 1', '≤ 2', '≤ 1', '≤ 0.5/9.5 | 1/19–2/38 | ≥ 4/76'],

                     ['≤ 1  |  2 | ≥ 4', '≤ 2/1 | – | ≥ 4/2', '≤ 2/1 | 4/2 | ≥ 8/4', 'not reported', '≤ 1/4 | – | ≥ 2/4', 'not reported', 'not reported', 'not reported', 'not reported', 
                        '≤ 2', '≤ 2', '≤ 2', '≤ 4 | 8 | ≥ 16', '≤ 2', '≤ 0.5', 'not reported', '≤ 2', '≤ 0.5', '≤ 0.5', 'not reported', 'not reported', 'not reported', '≤ 4', '≤ 8 | 16 | ≥ 32', '≤ 2 | 4 | ≥ 8',
                        'not reported', 'not reported', '≤ 1', '≤ 2', '≤ 1', '≤ 0.5/9.5 | 1/19–2/38 | ≥ 4/76'], ['≤ 8 | 16 | ≥ 32', '≤ 8/4 | 16/8 | ≥ 32/16',	'≤ 8/4 | 16/8 | ≥ 32/16','≤ 2/4 | 4/4 | ≥ 8/4',	'≤ 8/4 | 16/4 | ≥ 32/4', '≤ 8/4 | – | ≥ 16/4',	'≤ 4/8 | 8/8 | ≥ 16/8',	'≤ 2 | 4 | ≥ 8', '≤ 16 | – | ≥ 32', '≤ 1 |2 | ≥ 4', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', 
                    '≤ 8 | 16 | ≥ 32', '≤ 2 | 4-8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', 
                        '≤ 2 | 4 | ≥ 8', '≤ 2 | 4 | ≥ 8', 'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.25 | 0.5 | ≥ 1', 
                        '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],

                      [ '≤ 8 | 16 | ≥ 32',	'≤ 8/4 | 16/8 | ≥ 32/16', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 2/4 | 4/4 | ≥ 8/4', '≤ 8/4 | 16/4 | ≥ 32/4', '≤ 8/4 | – | ≥ 16/4', '≤ 4/8 | 8/8 | ≥ 16/8', 
                        '≤ 2 | 4 | ≥ 8', '≤ 16 | – | ≥ 32', '≤ 1 |2 | ≥ 4', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 8 | 16 | ≥ 32', '≤ 2 | 4-8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 
                    '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 2 | 4 | ≥ 8', '≤ 2 | 4 | ≥ 8', 'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 
                    '≤ 0.25 | 0.5 | ≥ 1', '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],

                        ['≤ 8 | 16 | ≥ 32', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 2/4 | 4/4 | ≥ 8/4', '≤ 8/4 | 16/4 | ≥ 32/4',
                        '≤ 8/4 | – | ≥ 16/4', '≤ 4/8 | 8/8 | ≥ 16/8', '≤ 2 | 4 | ≥ 8', '≤ 16 | – | ≥ 32', '≤ 1 |2 | ≥ 4', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 8 | 16 | ≥ 32', 
                        '≤ 2 | 4-8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', 
                    '≤ 2 | 4 | ≥ 8', '≤ 2 | 4 | ≥ 8', 'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.25 | 0.5 | ≥ 1', '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],

                        ['≤ 8 | 16 | ≥ 32', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 2/4 | 4/4 | ≥ 8/4', '≤ 8/4 | 16/4 | ≥ 32/4',
                        '≤ 8/4 | – | ≥ 16/4', '≤ 4/8 | 8/8 | ≥ 16/8', '≤ 2 | 4 | ≥ 8', '≤ 16 | – | ≥ 32', '≤ 1 |2 | ≥ 4', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 8 | 16 | ≥ 32', 
                        '≤ 2 | 4-8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 2 | 4 | ≥ 8', '≤ 2 | 4 | ≥ 8', 
                        'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.25 | 0.5 | ≥ 1', '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],



                     ['≤ 8 | 16 | ≥ 32', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 2/4 | 4/4 | ≥ 8/4', '≤ 8/4 | 16/4 | ≥ 32/4', '≤ 8/4 | – | ≥ 16/4', '≤ 4/8 | 8/8 | ≥ 16/8',
                        '≤ 2 | 4 | ≥ 8', '≤ 16 | – | ≥ 32', '≤ 1 |2 | ≥ 4', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 8 | 16 | ≥ 32', '≤ 2 | 4-8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 
                    '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 2 | 4 | ≥ 8', '≤ 2 | 4 | ≥ 8', 'not reported', 'not reported', 	'≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 
                        '≤ 0.25 | 0.5 | ≥ 1', '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],

                      ['≤ 8 | 16 | ≥ 32', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 2/4 | 4/4 | ≥ 8/4', '≤ 8/4 | 16/4 | ≥ 32/4', '≤ 8/4 | – | ≥ 16/4', '≤ 4/8 | 8/8 | ≥ 16/8', 
                        '≤ 2 | 4 | ≥ 8', '≤ 16 | – | ≥ 32', '≤ 1 |2 | ≥ 4', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 8 | 16 | ≥ 32', '≤ 2 | 4-8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 
                        '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 2 | 4 | ≥ 8', '≤ 2 | 4 | ≥ 8', 'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 
                        '≤ 0.25 | 0.5 | ≥ 1', '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],

                     ['≤ 8 | 16 | ≥ 32', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 2/4 | 4/4 | ≥ 8/4', '≤ 8/4 | 16/4 | ≥ 32/4', '≤ 8/4 | – | ≥ 16/4', '≤ 4/8 | 8/8 | ≥ 16/8', 
                        '≤ 2 | 4 | ≥ 8', '≤ 16 | – | ≥ 32', '≤ 1 |2 | ≥ 4', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 8 | 16 | ≥ 32', '≤ 2 | 4-8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 
                        '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 2 | 4 | ≥ 8', '≤ 2 | 4 | ≥ 8', 'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16',
                        '≤ 0.25 | 0.5 | ≥ 1', '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],

                    ['≤ 8 | 16 | ≥ 32', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported' ,'≤ 1 |2 | ≥ 4', 
                    '≤ 1 |2 | ≥ 4', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', 'not reported', 'not reported', 
                        'not reported', 'S. enterica ser. Typhi only ≤ 16 |– |≥ 32', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.06 | 0.12- 0.5 | ≥ 1', '≤ 0.12 | 0.25- 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],


                      ['≤ 8 | 16 | ≥ 32', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', '≤ 1 |2 | ≥ 4', 
                     '≤ 1 |2 | ≥ 4', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', 'not reported', 'not reported', 
                        'not reported', '≤ 8 | 16 | ≥ 32', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.25 | 0.5 | ≥ 1', '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],



                     ['not reported', 'not reported', 'not reported', '≤ 4/4 | 8/4 | ≥ 16/4', '≤ 16/4 | 32/4 | ≥ 64/4', '≤ 8/4 | – | ≥ 16/4', 'not reported', 'not reported', 
                        'not reported', 'not reported', 'not reported', '≤ 8 | 16 | ≥ 32', 'not reported', '≤ 8 | 16 | ≥ 32', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 8 | 16 | ≥ 32', 'not reported',
                        '≤ 2 | 4 | ≥ 8', '≤ 16 | 32 | ≥ 64', 'not reported', '≤ 1 |2 | ≥ 4', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', 'not reported', 'not reported'],



                     ['not reported', '≤ 8/4 | 16/8 | ≥ 32/16', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 
                        '≤ 8 | 16–32 | ≥ 64', '≤ 8 | 16–32 | ≥ 64', '≤ 8 | 16 | ≥ 32', 'not reported', '≤ 8 | 16 | ≥ 32', 'not reported', '≤ 4 | 8 | ≥ 16', 'not reported', 'not reported', 
                    '≤ 2 | 4 | ≥ 8', '≤ 16 | 32 | ≥ 64', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 1 |2 | ≥ 4', '≤ 2 | 4 | ≥ 8', 'not reported', '≤ 2/38 | – | ≥ 4/76'],


                      ['not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 
                    'not reported', 'not reported', '≤ 8 | 16 | ≥ 32', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', 'not reported', 'not reported', 
                        'not reported', 'not reported', 'not reported', 'not reported', 'not reported', '≤ 4 | 8  | ≥ 16', 'not reported', '≤ 2 | 4 | ≥ 8', 'not reported', '≤ 2/38 | – | ≥ 4/76'],



                     ['not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported',
                        'not reported', 'not reported', 'not reported', 'not reported', 'not reported', '≤ 1', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 'not reported', 
                        'not reported', 'not reported', 'not reported', 'not reported', '≤ 1 | 2 | ≥ 4', 'not reported', '≤ 2 | 4 | ≥ 8', 'not reported', '≤ 2/38 | – | ≥ 4/76'],


                      ['≤ 1  |  2 | ≥ 4', '≤ 2/1 | – | ≥ 4/2', '≤ 2/1 | 4/2 | ≥ 8/4', '≤ 0.5/4', '≤ 1/4 | – | ≥ 2/4', 'not reported', 'not reported', 'not reported', 'not reported', 
                        '≤ 2', '≤ 2', '≤ 2', '≤ 4 | 8 | ≥ 16', '≤ 2', '≤ 0.5', 'not reported', '≤ 2', '≤ 0.5', '≤ 0.5', 'not reported', 'not reported', 'not reported', '≤ 4', '≤ 8 | 16 | ≥ 32', '≤ 2 | 4 | ≥ 8',
                        'not reported', 'not reported', '≤ 1', '≤ 2', '≤ 1', '≤ 0.5/9.5 | 1/19–2/38 | ≥ 4/76'],

                     ['≤ 1  |  2 | ≥ 4', '≤ 2/1 | – | ≥ 4/2', '≤ 2/1 | 4/2 | ≥ 8/4', 'not reported', '≤ 1/4 | – | ≥ 2/4', 'not reported', 'not reported', 'not reported', 'not reported', 
                        '≤ 2', '≤ 2', '≤ 2', '≤ 4 | 8 | ≥ 16', '≤ 2', '≤ 0.5', 'not reported', '≤ 2', '≤ 0.5', '≤ 0.5', 'not reported', 'not reported', 'not reported', '≤ 4', '≤ 8 | 16 | ≥ 32', '≤ 2 | 4 | ≥ 8',
                        'not reported', 'not reported', '≤ 1', '≤ 2', '≤ 1', '≤ 0.5/9.5 | 1/19–2/38 | ≥ 4/76'],
     ['≤ 8 | 16 | ≥ 32', '≤ 8/4 | 16/8 | ≥ 32/16',	'≤ 8/4 | 16/8 | ≥ 32/16','≤ 2/4 | 4/4 | ≥ 8/4',	'≤ 8/4 | 16/4 | ≥ 32/4', '≤ 8/4 | – | ≥ 16/4',	'≤ 4/8 | 8/8 | ≥ 16/8',	'≤ 2 | 4 | ≥ 8', '≤ 16 | – | ≥ 32', '≤ 1 |2 | ≥ 4', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', 
                    '≤ 8 | 16 | ≥ 32', '≤ 2 | 4-8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', 
                        '≤ 2 | 4 | ≥ 8', '≤ 2 | 4 | ≥ 8', 'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 0.25 | 0.5 | ≥ 1', 
                        '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],
     [ '≤ 8 | 16 | ≥ 32',	'≤ 8/4 | 16/8 | ≥ 32/16', '≤ 8/4 | 16/8 | ≥ 32/16', '≤ 2/4 | 4/4 | ≥ 8/4', '≤ 8/4 | 16/4 | ≥ 32/4', '≤ 8/4 | – | ≥ 16/4', '≤ 4/8 | 8/8 | ≥ 16/8', 
                        '≤ 2 | 4 | ≥ 8', '≤ 16 | – | ≥ 32', '≤ 1 |2 | ≥ 4', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 8 | 16 | ≥ 32', '≤ 2 | 4-8 | ≥ 16', '≤ 0.5 | 1 | ≥ 2', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 
                    '≤ 0.5 | 1 | ≥ 2', '≤ 1 |2 | ≥ 4', '≤ 4 | 8 | ≥ 16', '≤ 2 | 4 | ≥ 8', '≤ 2 | 4 | ≥ 8', 'not reported', 'not reported', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', '≤ 4 | 8 | ≥ 16', 
                    '≤ 0.25 | 0.5 | ≥ 1', '≤ 0.5 | 1 | ≥ 2', 'not reported', '≤ 2/38 | – | ≥ 4/76'],
     ]


Antibiotics= ['Ampicillin', 'Ampicillin-sulbactam', 'Amoxicillin-clauvulanate', 'Ceftolozane-tazobactam', 'Piperacillin-tazobactam',
                       
                       'Ceftazidime-Avibactam', 'Meropenem-vabormere','Cefazolin-non urine', 'Cefazolin urine', 


                        'Cefotaxime', 'Ceftriaxone','Ceftazidime', 'Cefuroxime', 'Cefepime', 'Ceftaroline', 'Cefiderocol', 'Aztreonam','Ertapenem', 'Meropenem', 'Amikacin', 'Gentamicin','Tobramycin','Azithromycin',	'Clarithromycin', 'Tetracycline', 'Doxycycline', 'Minocycline', 'Ciprofloxacin',	
                        'Levofloxacin','Moxifloxacin','Trimethoprim-sulfamethoxazole']


Organism= [ 'Escherichia coli','Klebseilla pneumoniae',
 'Klebseilla oxytoca','Proteus mirabilis',
 'Proteus spp, not mirabilis',
 'Enterobacter cloacae complex',
               'Klebseilla (formerly Enterobacter) aerogenes',
               'Salmonella','Shigella',
              'Pseudomonas aeruroginosa','Acinetobacter spp.',
              
 'Burkholderia cepacia complex',
 'Stenotrophomonas maltophila',
 'Haemophilus influenzae',
'Haemophilus parainfluenzae','Escherichia coli','Klebseilla pneumoniae',
 'Klebseilla oxytoca','Proteus mirabilis',
 'Proteus spp, not mirabilis',
 'Enterobacter cloacae complex',
               'Klebseilla (formerly Enterobacter) aerogenes',
               'Salmonella','Shigella',
              'Pseudomonas aeruroginosa','Acinetobacter spp.',
              
 'Burkholderia cepacia complex',
 'Stenotrophomonas maltophila',
 'Haemophilus influenzae',
'Haemophilus parainfluenzae','Escherichia coli','Klebseilla pneumoniae']

df2 = pd.DataFrame(data = MIC,  
                  index = Organism,  
                  columns = Antibiotics) 

df2['Organism']=df2.index
df2 = df2.reset_index(drop=True)


df2.set_index('Organism')

st.header(':red[Antibiotic Breakpoint Explorer 1.0]')
st.subheader(':violet[(Gram-negative bacteria)]')
st.sidebar.text('Organisms')

# Sidebar

def main():
     
  st.sidebar.title('')
organism_radio = st.sidebar.radio(':green[Select Organism]', df2.Organism.unique())
antib_search = st.sidebar.text_input('')

st.text('Value format: Sensitive|Intermediate|Resistant')
# Filtering based on selections
filtered_df = df2[(df2.Organism== organism_radio) & (df2.columns.str.contains(antib_search, case=False))]

filt_df= filtered_df[:1]


    # Displaying results
if not filt_df.empty:
    st.write(':blue[###Results: MIC values in µg/ml (CLSI)]')
    st.table(filt_df)
else:
        st.write('No results found.')

if __name__ == "__main__":
    main()

  



                   
