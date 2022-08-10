def checkIfPangram(self, sentence: str) -> bool:
    newSentence = set();

    for indivChar in sentence:
        newSentence.add(indivChar);

    return len(newSentence) == 26;

