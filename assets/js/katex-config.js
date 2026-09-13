function fixLatex(math) {
  // Normalize escaped braces \{ and \} or \\{ into { and }
  let m = math.replace(/\\+([{}])/g, "$1");
  // Normalize commands with excessive backslashes like \\text or \\frac into \text or \frac
  m = m.replace(/\\+([a-zA-Z]+)/g, "\\$1");
  // Replace unescaped _ inside \text{...} with \_
  m = m.replace(/\\text\{([^}]*)\}/g, (match, inner) => {
    return "\\text{" + inner.replace(/(?<!\\)_/g, "\\_") + "}";
  });
  return m;
}

function renderAllMath() {
  if (typeof window.renderMathInElement === "function" && document.body) {
    window.renderMathInElement(document.body, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false },
        { left: "\\(", right: "\\)", display: false },
        { left: "\\[", right: "\\]", display: true },
      ],
      preProcess: fixLatex,
      throwOnError: false,
    });
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", renderAllMath);
} else {
  renderAllMath();
}
