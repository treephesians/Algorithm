const fs = require("fs");

class TreeNode {
    constructor(spots, arrival) {
        this.spots = spots;
        this.arrival = arrival;
        this.left = null;
        this.right = null;
    }
}

class BST {
    constructor() {
        this.root = null;
        this.mostUnstableNode = null;
        this.maxInstability = -1;
        this.earliestArrival = Infinity;
    }

    insert(spots, arrival) {
        if (!this.root) {
            this.root = new TreeNode(spots, arrival);
        } else {
            let current = this.root;
            while (true) {
                if (spots < current.spots) {
                    if (!current.left) {
                        current.left = new TreeNode(spots, arrival);
                        break;
                    }
                    current = current.left;
                } else {
                    if (!current.right) {
                        current.right = new TreeNode(spots, arrival);
                        break;
                    }
                    current = current.right;
                }
            }
        }
    }

    getHeight(node) {
        if (!node) return 0;
        const leftHeight = this.getHeight(node.left);
        const rightHeight = this.getHeight(node.right);
        const instability = Math.abs(leftHeight - rightHeight);

        if (
            instability > this.maxInstability ||
            (instability === this.maxInstability && node.arrival < this.earliestArrival)
        ) {
            this.maxInstability = instability;
            this.mostUnstableNode = node.spots;
            this.earliestArrival = node.arrival;
        }

        return Math.max(leftHeight, rightHeight) + 1;
    }

    findMostUnstable() {
        this.getHeight(this.root);
        return this.mostUnstableNode;
    }
}

// ✅ 입력 처리
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
let index = 0;
const numFlocks = parseInt(input[index++]);
let output = [];

for (let flockNum = 1; flockNum <= numFlocks; flockNum++) {
    const numBirds = parseInt(input[index++]);
    const spots = input[index++].split(" ").map(Number);

    const bst = new BST();
    for (let i = 0; i < numBirds; i++) {
        bst.insert(spots[i], i);
    }

    output.push(`Flock #${flockNum}: ${bst.findMostUnstable()}\n`);
}

// ✅ 정답 출력
console.log(output.join("\n"));