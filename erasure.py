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
    #get 900 lines from baraka
    for line in baraka[10:1000]:
        clean_line = line.strip()
        if (len(clean_line) > 1) :
            good_index = 0
            output_phrase = []
            # for each line, check each tweet in order for matches
            for row in fascismreader:
                # get words from Bad Text
                bad_words = row['text'].split()
                for word in bad_words:
                # get characters from Bad Words and try to match next character in good text
                    #fucked this up by trying to split for a very long time, was only getting full words, guess you can't split a word with no delimiter?
                    # letters = word.split()
                    letters = list(word)
                    for letter in letters:
                        if (good_index < len(clean_line)):
                        #compare current letter in line from baraka text with letters in tweet, if it hits, add to output, otherwise add a space
                            if letter == clean_line[good_index]:
                                output_phrase.append(clean_line[good_index])
                                good_index += 1
                            elif (good_index >= 1):
                                output_phrase.append(" ")
                # once our output_phrase "tweet" hits 280 chars, add it to our output array and then reset it
                if (len(output_phrase) >= 280):
                    #make sure it's not totally blank
                    if (len("".join(output_phrase).strip()) > 0) :
                        outputrows.append("".join(output_phrase))

                    output_phrase = []
output = {'tweets': outputrows}
print('output: ', output)
json_output = json.dumps(output, indent=4)
with open("output.json", "w") as outfile:
    outfile.write(json_output)





