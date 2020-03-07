scoreDict = {}
maxScoreDict = {}
minScoreDict = {}
arrayMaxDict = {}
arrayMinDict = {}



def updateMaxArray(picture, new_picture, cur_score):

    if picture[0] in arrayMaxDict:
        if arrayMaxDict[picture[0]][0] == 100:
            arrayMaxDict[picture[0]][1][99] = [new_picture[0], cur_score]
            sorted(arrayMaxDict[picture[0]][1], key=lambda x: x[1], reverse=True)
        else:
            arrayMaxDict[picture[0]][1][arrayMaxDict[picture[0]][0]] = [new_picture[0], cur_score]
            sorted(arrayMaxDict[picture[0]][1], key=lambda x:x[1], reverse=True)
            arrayMaxDict[picture[0]][0] += 1
    else:
        arrayMaxDict[picture[0]] = [0, []]


def updateMinArray(picture, new_picture, cur_score):

    if picture[0] in arrayMaxDict:
        if arrayMaxDict[picture[0]][0] == 100:
            arrayMaxDict[picture[0]][1][99] = [new_picture[0], cur_score]
            sorted(arrayMaxDict[picture[0]][1], key=lambda x: x[1])
        else:
            arrayMaxDict[picture[0]][1][arrayMaxDict[picture[0]][0]] = [new_picture[0], cur_score]
            sorted(arrayMaxDict[picture[0]][1], key=lambda x:x[1])
            arrayMaxDict[picture[0]][0] += 1
    else:
        arrayMaxDict[picture[0]] = [0, []]


def updateMax():


def updateMin():


def updateDict(deleted_picture):

    for x in maxScoreDict:
        if deleted_picture[0] != maxScoreDict[x]:
            updateMax()

    for x in minScoreDict:
        if deleted_picture[0] != minScoreDict[x]:
            updateMin()


def score(picture1, picture2):

    tuple1 = (picture1[0], picture2[0])
    tuple2 = (picture2[0], picture1[0])

    if tuple1 in scoreDict:
        return scoreDict[tuple1]
    elif tuple2 in scoreDict:
        return scoreDict[tuple2]
    else:
        scoreDict[tuple1] = calc_score(picture1[2], picture2[2])
        return scoreDict[tuple1]


def calc_score(slide1, slide2):

    common_list = list(set(slide1).intersection(slide2))
    size_of_common_list = len(common_list)
    size_of_slide1 = len(slide1)
    size_of_slide2 = len(slide2)

    number1 = size_of_common_list
    number2 = size_of_slide1 - size_of_common_list
    number3 = size_of_slide2 - size_of_common_list

    #print "number1", number1
    #print "number2", number2
    #print "number3", number3

    return min(number1, number2, number3)


#def total_score_vertical(all_pictures):
#
#    num_of_picture = len(all_pictures)
#
#    for



def total_score_horizontal(all_pictures):

    num_of_picture = len(all_pictures)

    for picture in all_pictures:
        sum_score = 0
        min_score = 101
        max_score = -1
        max_id = -1
        min_id = -2
        for new_picture in all_pictures:
            #print "new_picture:", new_picture
            #print "picture:", picture
            if new_picture[0] is picture[0]:
                continue
            cur_score = score(picture, new_picture)
            sum_score += cur_score

            if cur_score > max_score:
                max_score = cur_score
                max_id = new_picture[0]
            if cur_score < min_score:
                min_score = cur_score
                min_id = new_picture[0]

            #print "score: ", score(picture, new_picture)
        picture.append(sum_score)
        maxScoreDict[picture[0]] = max_id
        minScoreDict[picture[0]] = min_id
        updateArray(picture, new_picture, cur_score)
        #print "sum_score: ", picture[3]

    return all_pictures


if __name__ == '__main__':

    slide1 = [0, 'V', ['cat', 'dog', 'house', 'blabla', 'meow']]
    slide2 = [1, 'H', ['house', 'dog', 'foo', 'bla']]
    slide3 = [2, 'V', ['cat', 'foo', 'house', 'bla']]
    slide4 = [3, 'V', ['house', 'dog', 'cat', 'foo']]

    all_pictures = []
    all_pictures.append(slide1)
    all_pictures.append(slide2)
    all_pictures.append(slide3)
    all_pictures.append(slide4)

    #print all_pictures
    #min_number = score(slide1, slide2)
    final_list = total_score_horizontal(all_pictures)

    print "lists: ", final_list

    for i in scoreDict:
        print i, scoreDict[i]

    #for x in scoreDict:
    #    print x
    #    for y in scoreDict[x]:
    #        print y, ":", scoreDict[x][y]
