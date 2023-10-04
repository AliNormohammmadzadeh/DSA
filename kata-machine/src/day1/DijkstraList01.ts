function hasUnvisited(seen: boolean[], dists: number[]): boolean {
    // Log information about seen and dists
    console.log('seen:', seen);
    console.log('dists:', dists);
    
    return seen.some((s, i) => !s && dists[i] < Infinity);
}

function getLowestUnvisited(seen: boolean[], dists: number[]): number {
    let idx = -1;
    let lowestDistance = Infinity;

    for (let i = 0; i < seen.length; i++) {
        if (seen[i]) {
            continue;
        }

        if (lowestDistance > dists[i]) {
            lowestDistance = dists[i];
            idx = i;
        }
    }

    // Log information about seen and dists
    console.log('seen:', seen);
    console.log('dists:', dists);
    
    return idx;
}

export default function dijkstra_list(source: number, sink: number, arr: WeightedAdjacencyList): number[] {
    const seen = new Array(arr.length).fill(false);
    const prev = new Array(arr.length).fill(-1);
    const dists = new Array(arr.length).fill(Infinity);
    dists[source] = 0;

    // Log information about source, sink, and arr
    console.log('source:', source);
    console.log('sink:', sink);
    console.log('arr:', arr);

    while (hasUnvisited(seen, dists)) {
        const curr = getLowestUnvisited(seen, dists);

        seen[curr] = true;

        // Log information about the current node and seen
        console.log('Current Node:', curr);
        console.log('seen:', seen);
        
        const adjs = arr[curr];
        for (let i = 0; i < adjs.length; i++) {
            const edge = adjs[i];

            // Log information about adjs and edge
            console.log('adjs:', adjs);
            console.log('edge:', edge);

            if (seen[edge.to]) {
                continue;
            }

            const dist = dists[curr] + edge.weight;
            if (dist < dists[edge.to]) {
                dists[edge.to] = dist;
                prev[edge.to] = curr;
            }
        }
    }

    // Log information about prev and dists
    console.log('prev:', prev);
    console.log('dists:', dists);

    const out: number[] = [];
    let curr = sink;
    while (prev[curr] !== -1) {
        out.push(curr);
        curr = prev[curr];
    }

    out.push(source);

    // Log the final output path
    console.log('Shortest Path:', out.reverse());

    return out.reverse();
}
