def q1(answer):
    if answer.upper() == "ATGCTTCGGAT":
        return "Correct, well done!"
    else:
        print("Try again.\nRemember, the smaller fragments travel further towards the positive side, so you'll want to start reading from there.")

def q2(answer):
    if answer.upper() == "AGGACTTTGACAT":
        return "Nice job!"
    else:
        print("Try again.\nRemember, the smaller fragments travel further towards the positive side, so you'll want to start reading from there.")

def q3(answer):
    if answer.upper() == "CTGGACTCAAGTT":
        return "Great!"
    else:
        print("This one is a bit more difficult. Notice how some bands are thicker, but have distinctions between the two.\nThat can mean two of the same nuncleotide are next to one another.")

def q4(answer):
    if answer.upper() == "B":
        return "Correct"
    else:
        return "Try Again"

def q5(answer):
    if answer.upper() == "DI" or answer.upper() == "DI.fq":
        return "Excellent, the overrepresented sequences are the adapters"
    else:
        return "If sequences show up very often, it could be that they were used to attach to the reads..."