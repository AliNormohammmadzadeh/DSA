function qs(arr: number[] , lo: number, hi: number): void{
    if(lo >= hi){
        return
    }

    const privotIdx = partition(arr, lo , hi)

    qs(arr , lo , privotIdx - 1)
    qs(arr , privotIdx + 1, hi)
}

function partition(arr: number[] , lo:number , hi: number ):number {
    const privot = arr[hi];

    let idx = lo - 1;
    for(let i= lo ; i < hi ; i++){
        if(arr[i] <= privot){
            idx++;
            const temp = arr[i];
            arr[i] = arr[idx];
            arr[idx] = temp
        }
    }

    idx++;
    arr[hi] = arr[idx]
    arr[idx] = privot

    return idx
}

export default function quick_sort(arr: number[]): void {
    qs(arr , 0 , arr.length - 1)
}