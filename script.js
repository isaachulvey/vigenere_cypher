document.addEventListener('DOMContentLoaded', () => {
    const messageInput = document.getElementById('message');
    const keyInput = document.getElementById('key');
    const resultOutput = document.getElementById('result');
    const encryptBtn = document.getElementById('encryptBtn');
    const decryptBtn = document.getElementById('decryptBtn');
    const resetBtn = document.getElementById('resetBtn');

    const ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

    function cleanup(text) {
        // Python version:
        // clean = text.replace(" ", "").upper().translate(str.maketrans('', '', string.punctuation))
        // return ''.join([i for i in clean if not i.isdigit()])

        const punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~';
        let clean = text.split(' ').join('').toUpperCase();

        let translated = '';
        for (let char of clean) {
            if (!punctuation.includes(char)) {
                translated += char;
            }
        }

        let final = '';
        for (let char of translated) {
            if (char < '0' || char > '9') {
                final += char;
            }
        }
        return final;
    }

    function getVigenereResult(message, key, mode) {
        const cleanMessage = cleanup(message);
        const cleanKey = cleanup(key);

        if (!cleanMessage || !cleanKey) {
            return '';
        }

        let result = '';
        const keyLen = cleanKey.length;

        for (let i = 0; i < cleanMessage.length; i++) {
            const mChar = cleanMessage[i];
            const kChar = cleanKey[i % keyLen];

            const mIdx = ALPHABET.indexOf(mChar);
            const kIdx = ALPHABET.indexOf(kChar);

            // In the Python code, if a character is not in alphabet (though cleanup should handle it),
            // it would fail in __get_key.
            // Our cleanup handles most cases, but let's be safe.
            if (mIdx === -1 || kIdx === -1) continue;

            let resIdx;
            if (mode === 'encrypt') {
                resIdx = (mIdx + kIdx) % 26;
            } else {
                resIdx = (mIdx - kIdx + 26) % 26;
            }
            result += ALPHABET[resIdx];
        }
        return result;
    }

    encryptBtn.addEventListener('click', () => {
        const message = messageInput.value;
        const key = keyInput.value;
        if (!cleanup(key)) {
            alert('Please enter a valid key (at least one letter)');
            return;
        }
        resultOutput.value = getVigenereResult(message, key, 'encrypt');
    });

    decryptBtn.addEventListener('click', () => {
        const message = messageInput.value;
        const key = keyInput.value;
        if (!cleanup(key)) {
            alert('Please enter a valid key (at least one letter)');
            return;
        }
        resultOutput.value = getVigenereResult(message, key, 'decrypt');
    });

    resetBtn.addEventListener('click', () => {
        messageInput.value = '';
        keyInput.value = '';
        resultOutput.value = '';
    });
});
