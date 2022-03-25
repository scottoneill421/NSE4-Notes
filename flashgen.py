import sys, random, os



def usage():
    """prints usage to the user"""
    print("Please enter a file to parse")
    print("Example:     python3 quiz.py my-notes")
    print("Exiting...")


def getHeaders(file):
    """Get headers of notes file"""

    #get contents of file, remove excess newline characters
    content = file.readlines()
    content = list(filter(lambda x: x != '\n', content))

    #trim off title
    while content[0][0] == "=":
        item = content.pop(0)

    #format content into a list of headers and their notes
    buffer  = []
    headers = []
    for line in content:
        if line[0] == '\t':
            buffer.append(line)
        else:
            if len(buffer) != 0:
                headers.append(buffer)
                buffer = []
            buffer.append(line)
    headers.append(buffer)

    return headers


def getSubheaders(headers):
    """Get subheaders from a header list"""
    subheaders = []
    buffer = []
    #divide headers into their respective subheaders
    for header in headers:
        category = header.pop(0)
        for line in header:
            if line[1] == '\t':
                buffer.append(line)
            else:
                if len(buffer) > 1:
                    subheaders.append(buffer)
                    buffer = []
                buffer.append(category)
                buffer.append(line)
    subheaders.append(buffer)
    return subheaders

def getFlashcards(subheaders):
    """Generate flashcard dicts"""
    flashcards = []
    #generate flashcard objects using subheader objects
    for subheader in subheaders:
        flashcard = {
             "category": "",
             "question": "",
             "answer": [],
        }
        flashcard["category"] = subheader.pop(0)
        flashcard["question"] = subheader.pop(0)
        flashcard["answer"] = subheader
        flashcards.append(flashcard)
    return flashcards


def runQuiz(flashcards):
    """Presents each note as a flashcard"""
    while True:
        flashcard = flashcards[random.randint(0, (len(flashcards) - 1))]
        print(f'{flashcard["category"].strip()}:\t{flashcard["question"].strip()}')
        input()
        for i in flashcard["answer"]:
            print(f"\t\t{i.strip()}")
        input()
        os.system('clear')


def main():
    """the main routine to be run"""
    notes = [
        "antivirus.notes",
        "application-control.notes",
        "authentication.notes",
        "certificates.notes",
        "fsso.notes",
        "high-availability.notes",
        "ips.notes",
        "logging.notes",
        "nat.notes",
        "security-fabric.notes",
        "sslvpn.notes",
        "webfilter.notes",
    ]
    if len(notes) < 2:
        usage()
    else:
        flashcards = []
        for file in notes:
            with open(file, "r") as f:
                headers = getHeaders(f)
                subheaders = getSubheaders(headers)
                buffer = getFlashcards(subheaders)
                for i in buffer:
                    flashcards.append(i)
        
        runQuiz(flashcards)


if __name__ == '__main__':
    main()
