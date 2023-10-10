import load_data
import topicModel

if __name__ == "__main__":
    lines  = load_data.load_data()
    topicModel.gen_html(lines, 3, "lda.html")