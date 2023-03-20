function heightChecker(heights: number[]): number {
    const sorted = [...heights].sort((x,y) => x - y)
    let count = 0;
    for (let i = 0;i < heights.length;i++){
        if (sorted[i] !== heights[i]){
            count++
        }
    }
    return count
};