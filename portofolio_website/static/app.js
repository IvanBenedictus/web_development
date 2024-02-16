// Scroll feature
class Scroll {
    constructor() {
        this.nav = document.querySelector("#nav");
    }

    showNav() {
        this.nav.classList.add("show");
    }
    
    hideNav() {
        this.nav.classList.remove("show");
    }

    scrollFeature() {
        var currPos = window.scrollY;
        
        document.addEventListener("scroll", () => {
            if (window.scrollY <= currPos) {
            //scroll up
                this.hideNav();
            } else {
            //scroll down
                this.showNav();
            }
            currPos = window.scrollY;
        });

        let timeoutId

        document.addEventListener("click", () => {
            timeoutId = setTimeout(() => {
                this.hideNav();
            }, 1000);
        })
    }
}

const feature = new Scroll();
feature.scrollFeature();


// Chatbot feature
class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector(".chatboxButton"),
            chatBox: document.querySelector(".chatboxSupport"),
            sendButton: document.querySelector(".chatboxSend")
        }
        this.state = false;
        this.messages = [];
    }

    display() {
        const {openButton, chatBox, sendButton} = this.args;
        const node = chatBox.querySelector("input");

        openButton.addEventListener("click", () => chatBox.classList.toggle("active"))
        sendButton.addEventListener("click", () => this.onSendButton(chatBox))
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    onSendButton(chatbox) {
        var textField = chatbox.querySelector("input");
        let text = textField.value
        if (text === "") {
            return;
        }

        let msg1 = {name: "User", message: text}
        this.messages.push(msg1);

        fetch("/predict", {
            method: "POST",
            body: JSON.stringify({ message: text }),
            mode: "cors",
            headers: {"Content-Type": "application/json"},
        })

        .then(r => r.json())

        .then(r => {
            let msg2 = { name: "Bot", message: r.answer };
            this.messages.push(msg2);
            this.updateChatText(chatbox)
            textField.value = ""

        }).catch((error) => {
            console.error("Error:", error);
            this.updateChatText(chatbox)
            textField.value = ""
        });
    }

    updateChatText(chatbox) {
        var html = "";
        const chatmessage = chatbox.querySelector(".chatboxMessages");
        
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Bot") {
                html += "<div class='messagesItem visitor'>" + item.message + "</div>"
            } else {
                html += "<div class='messagesItem operator'>" + item.message + "</div>"
            }
        });

        chatmessage.innerHTML = html;
    }
}

const chatbox = new Chatbox();
chatbox.display();