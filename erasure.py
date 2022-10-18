import csv
import json
csv.register_dialect('piper', delimiter=',')
baraka = open("corpuses/sos_poems.txt").readlines()
print(len(baraka))
with open("corpuses/rondesantisfl_tweets.csv", newline='') as csvfile:
    #had some issue with iterable getting consumed where it could only get the first line - converting to a list fixes i think
    reader = csv.DictReader(csvfile, dialect = 'piper')
    fascismreader = list(reader)

    outputrows = []
    for line in baraka[0:500]:
        clean_line = line.strip()
        if (len(clean_line) > 1) :
            good_index = 0
            for row in fascismreader:
                output_phrase = []
                bad_words = row['text'].split()
                # get characters from bad text and try to match next character in good text
                for word in bad_words:
                    #fucked this up by trying to split for a very long time, was only gettuing full words, guess you can't split a word with no delimiter?
                    # letters = word.split()
                    letters = list(word)
                    for letter in letters:
#                            print('letter: ', letter)
#                            print('clean letter: ', clean_line[good_index])
                        if (good_index < len(clean_line)):
                            if letter == clean_line[good_index]:
                                output_phrase.append(clean_line[good_index])
                                good_index += 1
                            else:
                                output_phrase.append(" ")
                if (len("".join(output_phrase).strip())) > 0:
                    print('phrase len: ', len("".join(output_phrase).strip()))
                    outputrows.append("".join(output_phrase))
#                    print('letter found! ' "".join(output_phrase))
output = {'tweets': outputrows}
json_output = json.dumps(output, indent=4)
with open("output.json", "w") as outfile:
    outfile.write(json_output)
#





