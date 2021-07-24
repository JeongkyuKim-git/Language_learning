"""
3. K개로 구성된 DNA 염기 서열을 K-mer 라고 부릅니다. 예를 들어 1-mer 는 A, C, T, C 네 가지 조합이 가능하고,
2-mer 는 AA, AC, AG, AT, CC, CT, CA, CG, TT, TA, TC, TG, GG, GA, GC, GT 도합 16가지 조합이 가능합니다.
입력값 K 에 따라 모든 가능한 4k 개의 K-mer를  출력하는 것을 만들어라.
"""


def Make_kmer(k, listResult=['A', 'C', 'G', 'T']):
    listNucle = ['A', 'C', 'G', 'T']
    listTmp = []
    if k == 1:
        return listResult
    else:
        for nucle1 in listResult:
            for nucle2 in listNucle:
                listTmp.append(nucle1 + nucle2)
        return Make_kmer(k - 1, listTmp)


print(Make_kmer(2))



