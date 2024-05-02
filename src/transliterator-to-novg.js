// Граф симоволов взят с https://github.com/ogpetrov/sakha-nlp

function transliterateNovgorodov() {
  const graphs = {
    3: {
      ннь: "ɲ:",
      ддь: "dʑ:",
    },
    2: {
      ыа: "ɯa",
      иэ: "iɛ",
      үө: "yө",
      уо: "uɔ",
      нь: "ɲ",
      дь: "з",
      аа: "a:",
      оо: "ɔ:",
      уу: "u:",
      ыы: "ɯ:",
      ээ: "ɛ:",
      өө: "ө:",
      үү: "y:",
      ии: "i:",
      мм: "m:",
      нн: "n:",
      ҥҥ: "ŋ:",
      пп: "p:",
      тт: "t:",
      чч: "tɕ:",
      кк: "k:",
      бб: "b:",
      дд: "d:",
      гг: "g:",
      сс: "s:",
      хх: "q:",
      һһ: "h:",
      ҕҕ: "ʃ:",
      лл: "l:",
      йй: "j:",
      рр: "ɾ:",
      ль: "ʎ",
      вв: "v:",
      ee: "iɛ:",
      фф: "f:",
    },
    1: {
      а: "a",
      А: "А",
      о: "ɔ",
      О: "Ɔ",
      у: "u",
      У: "U",
      ы: "ɯ",
      Ы: "ɯ",
      э: "ɛ",
      Э: "E",
      ө: "ө",
      Ɵ: "Ɵ",
      ү: "y",
      Ү: "У",
      и: "i",
      И: "İ",
      м: "m",
      М: "M",
      н: "n",
      Н: "N",
      ҥ: "ŋ",
      Ң: "Ŋ",
      п: "p",
      П: "P",
      т: "t",
      Т: "T",
      ч: "c",
      Ч: "C",
      к: "k",
      К: "K",
      б: "b",
      Б: "B",
      д: "d",
      Д: "d",
      г: "g",
      Г: "G",
      с: "s",
      С: "S",
      х: "q",
      Х: "Q",
      һ: "h",
      Һ: "H",
      ҕ: "ʃ",
      Ҕ: "ʃ",
      л: "l",
      Л: "L",
      й: "j",
      Й: "j",
      р: "ɾ",
      Р: "ɾ",
      в: "v",
      В: "V",
      е: "iɛ",
      Е: "İɛ",
      ф: "f",
      Ф: "F",
    },
  };

  let phrase = document.getElementById("cyrillicInput").value;
  let transliteratedPhrase = "";
  let i = 0;
  let word = "";

  while (i < phrase.length) {
    let isFound = false;

    // check three-letters graphs
    if (
      i < phrase.length - 2 &&
      graphs[3] &&
      graphs[3][phrase.substring(i, i + 3)]
    ) {
      word += graphs[3][phrase.substring(i, i + 3)];
      i += 3;
      isFound = true;
    }

    // check two-letters graphs
    if (
      i < phrase.length - 1 &&
      graphs[2] &&
      graphs[2][phrase.substring(i, i + 2)]
    ) {
      word += graphs[2][phrase.substring(i, i + 2)];
      i += 2;
      isFound = true;
    }

    // check one-letters graphs
    if (!isFound && graphs[1] && graphs[1][phrase[i]]) {
      word += graphs[1][phrase[i]];
      i += 1;
      isFound = true;
    }

    // if not found, skip symbol
    if (!isFound) {
      i += 1;
    }

    // if word is complete, add it to the transliteratedPhrase and reset word
    if (isFound && (i === phrase.length || phrase[i] === " ")) {
      transliteratedPhrase += word + " ";
      word = "";
    }
  }

  // if there is a word left after the loop, add it to the transliteratedPhrase
  if (word) {
    transliteratedPhrase += word;
  }

  document.getElementById("latinOutput").value = transliteratedPhrase;
  document.getElementById("latinOutput").dispatchEvent(new Event("input"));
}

function switchVariation(element, flag) {
  let switchers = document.querySelectorAll(".header-subtitle a");
  switchers.forEach(function (switcher) {
    switcher.classList.remove("active");
  });

  if (flag === true) {
    transliterateNovgorodov();
  } else {
    transliterateLatin();
  }

  isNovgorodovVariation = flag;

  element.classList.add("active");
}
