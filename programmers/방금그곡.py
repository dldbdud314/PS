def replace_sharp(m):
    return m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    
def solution(music, musicinfos):
    music = replace_sharp(music)
    ans = []
    idx = 0
    for musicinfo in musicinfos:
        st, et, title, codes = musicinfo.split(',')
        codes = replace_sharp(codes)
        shr, smin = map(int, st.split(':'))
        ehr, emin = map(int, et.split(':'))
        t = (ehr * 60 + emin) - (shr * 60 + smin)
        m = (codes * (t // len(codes)) + codes[0 : (t % len(codes))])
        if music in m:
            ans.append([len(m), idx, title])
    if ans:
        return sorted(ans, key = lambda x: (-x[0], x[1]))[0][2]
    else:
        return "(None)"

