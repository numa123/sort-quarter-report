def bubbleSort(arr, n):
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j][3] > arr[j+1][3]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# [[550, 'Fight Club', '1999-10-15', 100853753], [680, 'Pulp Fiction', '1994-09-10', 213900000], [157336, 'Interstellar', '2014-11-05', 701729206], [118340, 'Guardians of the Galaxy', '2014-07-30', 772776600], [293660, 'Deadpool', '2016-02-09', 783100000], [27205, 'Inception', '2010-07-15', 825532764], [155, 'The Dark Knight', '2008-07-16', 1004558444], [24428, 'The Avengers', '2012-04-25', 1518815515], [299536, 'Avengers: Infinity War', '2018-04-25', 2052415039], [19995, 'Avatar', '2009-12-15', 2923706026]]