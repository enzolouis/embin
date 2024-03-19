const content = document.getElementById("content")

function copyClipboard() {
    textToCopy = ""
    Array.from(content.children).forEach(function(item, index) {
        textToCopy += item.innerText
    })
    navigator.clipboard.writeText(textToCopy)
}