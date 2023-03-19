function canConstruct(ransomNote: string, magazine: string): boolean {
    const vocab = {};
    
    for (let i = 0; i < magazine.length; i++) {
        const char = magazine[i];
        vocab[char] ? vocab[magazine[i]]++ : vocab[magazine[i]] = 1;
    }
    
    for (let i = 0; i < ransomNote.length; i++) {
        const char = ransomNote[i];
        if (vocab[char] === 0 || !vocab[char]) {
            return false;
        }
        vocab[char]--;
    }
    
    return true;
};