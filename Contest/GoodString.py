def cntGood(S : str) -> int:
        # code here
        cnt = 0
        for i in range(len(S)-1):
            st = ''
            for j in range(i+1,len(S)):
                st.join(S[i])
                st.join(S[j])
                print(st)
                # dec =int(st)
                # if dec % 2 != 0:
                #     cnt += 1
        return cnt

ans = cntGood('1234')
print(ans)