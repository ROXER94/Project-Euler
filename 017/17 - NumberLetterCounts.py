# Calculates the number of letters used in writing out all the numbers from 1 to 1000

OneTo9 = len('onetwothreefourfivesixseveneightnine')
TenTo19 = len('teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen')
Tens = len('twentythirtyfortyfiftysixtyseventyeightyninety')
OneTo99 = 10 * Tens + 9 * (OneTo9) + TenTo19
OneTo999 = 9 * 99 * len('hundredand') + 100 * (OneTo9) + 9 * len('hundred') + 10 * (OneTo99)
print(len('onethousand') + OneTo999)