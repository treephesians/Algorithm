class TrieNode {
    constructor() {
      this.children = {};
      this.count = 0; // 이 노드를 지나간 단어 수
    }
  }
  
  class Trie {
    constructor() {
      this.root = new TrieNode();
    }
  
    insert(word) {
      let node = this.root;
      for (let char of word) {
        if (!node.children[char]) {a
          node.children[char] = new TrieNode();
        }
        node = node.children[char];
        node.count += 1;
      }
    }
  
    getInputCount(word) {
      let node = this.root;
      let inputCount = 0;
      for (let char of word) {
        node = node.children[char];
        inputCount++;
        if (node.count === 1) break; // 여기서부터는 유일함
      }
      return inputCount;
    }
  }
  
  function solution(words) {
    const trie = new Trie();
  
    for (let word of words) {
      trie.insert(word);
    }
  
    let totalInputCount = 0;
    for (let word of words) {
      totalInputCount += trie.getInputCount(word);
    }
  
    return totalInputCount;
    
  }