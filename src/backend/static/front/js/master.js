function redirectTranslateLogin(lang) {
  let redirect_url = "/public/html/front/entrance/login_" + lang + ".html"
  document.location = redirect_url
}

// general_guide 妊娠中・出産後の出しわけ
function showPostnatalItems() {
  var postnatal_items = document.getElementById("postnatal-items");
  state = postnatal_items.style.display;
  if (state == "none") {
    postnatal_items.setAttribute("style", "display:block");
  }
}

function hidePostnatalItems() {
  var postnatal_items = document.getElementById("postnatal-items");
  state = postnatal_items.style.display;
  if (state == "block") {
    postnatal_items.setAttribute("style", "display:none");
  }
}
$(function () {
  // ブラウザバック
  $("a.browserBack").on("click", function () {
    history.back();
    return false;
  });
});

// general_guide 児童扶養手当の条件確認
$(function () {
  $('#childcare-allowance-condition').on("change", function () {
    const is_checked = $('#childcare-allowance-condition').prop('checked');
    if (is_checked) {
      // 児童扶養手当の質問表示
      $('#childcare-allowance-item').addClass('d-flex flex-column').removeClass('d-none');
    } else {
      // 児童扶養手当の質問非表示
      $('#childcare-allowance-item').addClass('d-none').removeClass('d-flex flex-column');
    }
  });
});

// general_guide 特別児童扶養手当の条件確認
$(function () {
  $('#special-allowance-condition').on("change", function () {
    const is_checked = $('#special-allowance-condition').prop('checked');
    if (is_checked) {
      // 特別児童扶養手当の質問表示
      $('#special-allowance-item').addClass('d-flex flex-column').removeClass('d-none');
    } else {
      // 特別児童扶養手当の質問非表示
      $('#special-allowance-item').addClass('d-none').removeClass('d-flex flex-column');
    }
  });
});

// general_guide 出生関連事前手続きの回答による出しわけ
$(function () {
  $('input[name="pre-application"]').on("change", function () {
    const is_checked = $('#pre-application-yes').prop('checked');
    if (is_checked) {
      $('#mynumber-item').addClass('d-flex flex-column').removeClass('d-none');
    } else {
      $('#mynumber-item').addClass('d-none').removeClass('d-flex flex-column');
    }
  });
});

// general_guide 未熟児の場合の出しわけ
$(function () {
  $('input[id="weight"]').on("change", function () {
    const weight = this.value;
    //2000g超え
    if (weight > 2000) {
      //入院が必要かの質問表示
      $('#hospitalization-item').addClass('d-flex flex-column').removeClass('d-none');
      $('#premature-item').addClass('d-none').removeClass('d-flex flex-column');
      // 2000g以下
    } else {
      // 入院が必要かの質問非表示
      $('#hospitalization-item').addClass('d-none').removeClass('d-flex flex-column');
      // 未熟児養育医療の質問表示
      $('#premature-item').addClass('d-flex flex-column').removeClass('d-none');
    }
  });
});

// general_guide 入院が必要な場合の出しわけ
$(function () {
  $('input[name="hospitalization"]').on("change", function () {
    const is_checked = $('#hospitalization-yes').prop('checked');
    // 入院必要->未熟児養育医療の質問表示
    if (is_checked) {
      $('#premature-item').addClass('d-flex flex-column').removeClass('d-none');
      // 入院不要->未熟児養育医療の質問非表示
    } else {
      $('#premature-item').addClass('d-none').removeClass('d-flex flex-column');
    }
  });
});

// general_guide 公的医療保険による出しわけ
$(function () {
  $('input[name="parent-insurance"]').on("change", function () {
    const employee_insurance = $('#employee-insurance').prop('checked');
    // 健康保険->出産手当金の質問表示
    if (employee_insurance) {
      $('#childbirth-allowance-item').addClass('d-flex flex-column').removeClass('d-none');
      // 出産手当金の質問非表示
    } else {
      $('#childbirth-allowance-item').addClass('d-none').removeClass('d-flex flex-column');
    }
  })
})

// input/date_pick共通
function openModal(type) {
  let modal_area_id = "#" + type + "-modal-area";
  $(modal_area_id).fadeIn();
}

function closeModal(type) {
  let modal_area_id = "#" + type + "-modal-area";
  $(modal_area_id).fadeOut();
}

/* date_pick.html用 */
$(function () {
  $('input[name="btlChck"]').change(function () {
    var is_checked = $(this).prop('checked');
    var parent = $(this).parents('tr');
    if (is_checked) {
      parent.addClass('table-secondary');
    } else {
      parent.removeClass('table-secondary');
    }
  });
});

// input.html用
const getGenderRadioButton = () => {
  let input_form_elements = document.getElementById("form");
  let genderRadioNodeList = input_form_elements.gender;
  // もっと抽象化したいけど、ここの要素の部分を引数でうまく扱えない
  // モックなのでそのままで行きます。
  return genderRadioNodeList;
};

//性別ラベルチェック時
const relationshipControl = (element) => {
  const selectRelationship = document.getElementById("relationship");
  const parentModalIcon = document.getElementById("modal-parent");

  // 性別によって何番目の子かのラベルを可変に
  let relationshipLabel = document.getElementById("relationship-label");
  if (element.value == "female") {
    relationshipLabel.textContent = "何人目の女の子ですか?";
  } else {
    relationshipLabel.textContent = "何人目の男の子ですか?";
  }

  if (parentModalIcon.getAttribute("style") === "display: none !important;") {
    console.log(parentModalIcon);
    parentModalIcon.removeAttribute("style");
  }

  if (selectRelationship.getAttribute("disabled") === "true") {
    selectRelationship.style.display = 'block';
    selectRelationship.removeAttribute("disabled");
    setRelationShipOption(selectRelationship);
  }
};

const setRelationShipOption = (select) => {
  const numberList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"];
  numberList.forEach((element) => {
    const option = document.createElement("option");
    option.value = element;
    option.textContent = element + "人目";
    select.appendChild(option);
  });
};

// 嫡出子のチェックによる制御
const legitimacyControl = () => {
  let input_form_elements = document.getElementById("form");
  let legitimacyRadioNodeList = input_form_elements.legitimacy;
  legitimacyRadioNodeList.forEach((element) => {
    let check = element.checked;
    let familyname_father = document.getElementById("family-name-father");
    let name_father = document.getElementById("name-father");
    let year_father = document.getElementById("fathers-year");
    let month_father = document.getElementById("fathers-month");
    let day_father = document.getElementById("fathers-day");
    // 父親の情報入力部分をdisableにする処理
    if (element.value === "notLegitimacy" && check) {
      if (familyname_father.getAttribute("disabled") === null) {
        familyname_father.setAttribute("disabled", "true");
        name_father.setAttribute("disabled", "true");
        year_father.setAttribute("disabled", "true");
        month_father.setAttribute("disabled", "true");
        day_father.setAttribute("disabled", "true");
      }
      // その逆の処理
    } else if (element.value === "legitimacy" && check) {
      familyname_father.removeAttribute("disabled");
      name_father.removeAttribute("disabled");
      year_father.removeAttribute("disabled");
      month_father.removeAttribute("disabled");
      day_father.removeAttribute("disabled");
    }
  });
};
// event_input 届出人選択
function changeNotificationForm(notifier_num) {
  const agentForm = document.getElementById("agent-form");
  if (notifier_num == 3) {
    agentForm.style.display = "block";
  } else {
    agentForm.style.display = "none";
  }
}
// event_input 電話選択
$(function () {
  $('body').on('change', '#phone_selected_form', function () {
    const selected_num = this.value;
    if (selected_num == '3') {
      $('#selected-num-text').addClass('d-flex').removeClass('d-none');
    } else {
      $('#selected-num-text').addClass('d-none').removeClass('d-flex');
    }
  })
})
// event_input 増額
function taxupNotificationForm(tax_up_num) {
  const taxupForm = document.getElementById("tax-up-form");
  if (tax_up_num == 2) {
    taxupForm.style.display = "block";
  } else {
    taxupForm.style.display = "none";
  }
}

// event_input 減額
function taxdownNotificationForm(tax_down_num) {
  const taxdownForm = document.getElementById("tax-down-form");
  if (tax_down_num == 10) {
    taxdownForm.style.display = "block";
  } else {
    taxdownForm.style.display = "none";
  }
}

// event_input 増額・減額児童用　追加ボタン
function addExample() {
  let elements = $('#target');
  //jQueryのオブジェクトのメソッドを使ってクローン
  copied = elements.children('.adding-element:last').clone(true);
  //クローンしたものの孫要素にある削除ボタンを表示
  copied.find('.del-btn').css('display', 'block');

  // let elements = document.getElementById("target");
  // let copied = elements.lastElementChild.cloneNode(true);
  elements.append(copied);
  return false;
}


// event_input 増額・減額児童用　削除ボタン
$(function () {
  $('.del-btn').click(function () {
    var parent = $(this).parents('.adding-element');
    parent.remove();
  });
});

// event_input 保険の種類選択用
$(function () {
  $('#insurance-form').change(function () {
    const selected_num = this.value;
    const selected_label = $('option:selected', this).text()

    // 何も選択されていなければ保険名・支部名フィールドの削除
    if (selected_num == '0' || selected_num == '1') {
      $('#insurance-selected-div').addClass('d-none').removeClass('d-flex');
      $('#insurance-branch-div').addClass('d-none').removeClass('d-flex');
      return false;
    }

    // 保険名フィールドの追加
    $('#insurance-selected-div').addClass('d-flex').removeClass('d-none');
    $('#insurance-selected-label').text(selected_label);

    // 支部のフィールド追加
    $('#insurance-branch-div').addClass('d-flex').removeClass('d-none');
  })
})

function changeNotificationForm(notifier_num) {
  const agentForm = document.getElementById("agent-form");
  if (notifier_num == 3) {
    agentForm.style.display = "block";
  } else {
    agentForm.style.display = "none";
  }
}

// event_input 画像アップロード
$(function () {
  $("input[type='file']").on("change", function () {
    var file = this.files[0];
    var image_tag = $(this).next()[0]
    var reader = new FileReader();
    reader.onload = (function (file) {
      return function () {
        image_tag.setAttribute("src", this.result)
        image_tag.setAttribute("title", file.name)
      };
    })(file);
    reader.readAsDataURL(file);
  });
});

// mypage.html用
const randomGreeting = () => {
  let msg = new Array();

  msg[0] = `<p>日野町では各地区の公民館を会場に、子育て中のお母さん達が中心になって子育てサロンを開催しています。
  <br/>親子で好きな遊びを楽しんだり、おしゃべりしてストレス発散したり、子育て中の仲間作りの場にもなっています。
  <br/>詳しくは<a href="http://www.town.shiga-hino.lg.jp/cmsfiles/contents/0000003/3125/2021kosodatesaronnsyoukai.pdf" target="_blank">こちらのリンク</a>をご確認ください。</p>`;

  msg[1] = `<p>日野町では妊婦の健康管理と子育て支援の一環として、妊婦健康診査費用の助成を行っています。</p>
  <p>詳しくは<a href="https://www.town.shiga-hino.lg.jp/contents_detail.php?co=cat&frmId=1839&frmCd=29-1-1-0-0" target="_blank" rel="noopener noreferrer">こちらのページ</a>をご確認ください。</p>
  `;

  msg[2] = `<p>出産育児一時金のお手続きがお済みでないようです。</p>
  <p>子どもが生まれたときは出産育児一時金が受けられます。</p>
  <p>詳しくは<a href="http://www.town.shiga-hino.lg.jp/contents_detail.php?co=kak&frmId=363" target="_blank">こちらのページ</a>をご確認ください。</p>
  `;

  msg[3] = `<p>3月23日はご予約いただいた来庁予定日です。
  <br/> お気をつけてお越しください。
  <br/>予約をキャンセルする場合は<a href="/public/html/under_development.html">こちらのページ</a>からお願いします。
  </p>
  `;

  let num = Math.floor(Math.random() * 19937) % msg.length;

  document.write(msg[num]);
};

// mixins 削除モーダル用
$(function () {
  $('body').on('click', '.procedure-modal', function () {
    var parent = $(this).parents('#table-card');
    $('#procedure-modalArea').fadeIn();


    $('#procedure-delete-yes').on('click', function () {
      parent.remove();
      checkProcedureContents();

      $('#procedure-modalArea').fadeOut();
    });
    $('#procedure-delete-no').on('click', function () {
      $('#procedure-modalArea').fadeOut();
    });
  });
});


// mixins 完了モーダル用
$(function () {
  $('body').on('click', '.procedure-check-modal', function () {
    var parent = $(this).parents('#table-card');
    $('#procedure-check-modalArea').fadeIn();


    $('#procedure-check-yes').on('click', function () {
      parent.remove();
      checkProcedureContents();
      $('#procedure-check-modalArea').fadeOut();
    });
    $('#procedure-check-no').on('click', function () {
      console.log(parent);
      $('#procedure-check-modalArea').fadeOut();
    });
  });
});


function checkProcedureContents() {
  var procedure_contents_num = $(".procedure-contents").find('.procedure-card').length;
  var no_procedure_id = $('#no-procedure');
  if (procedure_contents_num == 0) {
    no_procedure_id.removeClass('d-none');
  };
}




