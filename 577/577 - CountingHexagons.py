# Calculates the sum of the number of all regular hexagons that can be found in an equilateral triangle divided into n^2 equilateral triangles for 3 ≤ n ≤ 12345

print(sum(sum(i*(n-i+1)*(n-i+2)//6 for i in range(3,n+1,3)) for n in range(3,12346)))