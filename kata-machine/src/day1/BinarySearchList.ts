export default function bs_list(haystack: number[], needle: number): boolean {
    let l = 0 , h = haystack.length
    do {
        const m = Math.floor(l + (h-l)/2)
        const val = haystack[m]
        if (val === needle){
            return true
        }else if (val > needle){
            h = m
        }else{
            l = m + 1
        }
    }
    while( l < h)
    
    return false    
}   