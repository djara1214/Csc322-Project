Forums = "forums.txt"

commentList = []


# Todo: Plug into GUI
class Comment:
    id = 0
    comment = ""
    name = ""

    def __init__(self, commentId,i_comment,i_name):
        self.id = commentId
        self.comment = i_comment
        self.name = i_name

    def __str__(self):
        return self.name+": "+self.comment


# def addCommentTo1:
#     comment = tk.Entry(self.mainFrame, font=(self.subTitleFont, self.subTitleFontSize))
#     current_comment = ForumsData(0, comment, userClass.currentAccount.userName)
#     ForumPage1.append(current_comment)


def WriteToForum(comment):
    file = open(Forums, "a")
    values = comment
    file.write(str(comment.id) + "|" + comment.comment + "|" + comment.name)
    file.write("\n")
    file.close()


def censor(sentence):
    badwords = ["fuck","shit","hell","bitch","motherfucker","ass"]

    sentence = sentence.lower()
    sentence = sentence.split()

    for index, word in enumerate(sentence):
        if any(badword in word for badword in badwords):
            sentence[index] = "".join(['*' if c.isalpha() else c for c in word])

    return " ".join(sentence)


def AddComments(forumPage):
    global commentList
    commentList = []
    file = open(Forums, "r")
    for line in file:
        # String is split and variables are stored in list
        commentVars = line.split("|")
        if forumPage == int(commentVars[0]):
            commentList.append(Comment(int(commentVars[0]),commentVars[1],commentVars[2]))


if __name__ == '__main__':
    AddComments(1)

    for comment in commentList:
        print(comment)
