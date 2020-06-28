
$(document).ready(function(){
  $("#optionalForm").hide();
  $("#optionalText").click(function (){
    $("#optionalForm").show();
    $("#optionalText").hide();
    $("#nextStep").hide();
  })
  $("#nextStep").click(function (){
    $("[id$='TOTAL_FORMS']")[0].value = 0;
    $("input.btn").click();
  })
  $("input[type='text'], td textarea").each(function (){
    $(this).addClass("col-8");
  })

  $("td textarea").each(function (){
    $(this).each(function (){
      $(this.rows = "4");
    })
  })

  if($('#id_logger_wizard-current_step').val() == "Session"){
    $(".heading").text("Class Details");
    if($("#id_Session-ClassType"))$("#id_Session-ClassType").val("Class");
    $("#id_Session-ClassLengthminutes").val("60");
  }
  if($('#id_logger_wizard-current_step').val() == "Technique"){
    $(".heading").text("Techniques");
    $(".subheading").text("Every technique involves either a; transition - to either a new position or a submission; retention - to help maintain an advantagous position or defend against an opponents ");
    techniqueConstrains();
  }
  if($('#id_logger_wizard-current_step').val() == "PositionalSparring"){
    $(".heading").text("Positional Sparring");
    $(".subheading").text("Most sessions consist of techniques, positional sparring and regular sparring. You can log techniques and positional sparring here.");
  }
  if($('#id_logger_wizard-current_step').val() == "SessionRolling"){
    $(".heading").text("Rolling");
    $(".subheading").text("Every time you roll, you should train with people better than you, worse than you, and equal to you.");
    $("#id_SessionRolling-RollingPartners_Plus").val(0);
    $("#id_SessionRolling-RollingPartners_Equals").val(0);
    $("#id_SessionRolling-RollingPartners_Minus").val(0);
  }
  if($('#id_logger_wizard-current_step').val() == "SessionEvaluation"){
    $(".heading").text("Evaluation");
    $(".subheading").text("");
    $("#id_SessionEvaluation-injurySeverity").parent().parent().hide();
    $("#id_SessionEvaluation-NoteOnInjury").parent().parent().hide();
    sessionEvaluationConstrains();
  }



  $("option[value='Top']").attr("data_attribute","1");
  $("option[value='Bottom']").attr("data_attribute","1");
  $("option[value='Attack']").attr("data_attribute","2");
  $("option[value='Defend']").attr("data_attribute","2");

  bindOptionConstrains(0);

  node.base = document.querySelector('form table tbody').cloneNode(true);
})

var node = {
  html:"",
  get code() { return this.html; },
  set base(base) { this.html = base; },
};

function bindOptionConstrains(id){
  $("[id$='"+id+"-StartPosition")
  .change( function() {
    filterSelectOptions( $("[id$='TopBottomstart']").last(), "data_attribute", attributeMatcher( $(this).val() ) );
  });
  if($('#id_logger_wizard-current_step').val() == "Technique"){
    $("[id$='"+id+"-EndPosition")
    .change( function() {
      filterSelectOptions( $("[id$='TopBottomend']").last(), "data_attribute", attributeMatcher( $(this).val() ) );
    });
  }
}

function attributeMatcher(str){
  switch (str) {
    case "Back":
    case "LegEntanglement":
    case "Standing":
      return "2";
    default:
      return "1";
  }
}

function techniqueConstrains(){
  $("[id$=MoveType]")
  .change(function (){
    table = $(this).parent().parent().parent();
    if( $(this).val() == "Escape"){
      table.find("[id$=StartPosition]").parent().parent().hide();
      table.find("[id$=TopBottomstart]").parent().parent().hide();
      table.find("[id$=EndSubmission]").parent().parent().hide();
      table.find("[id$=StartPositionSubcategory]").parent().parent().hide();
      table.find("[id$=StartPosition]").val("");
      table.find("[id$=TopBottomstart]").val("");
      table.find("[id$=EndSubmission]").val("");
      table.find("[id$=StartPositionSubcategory]").val("");
      table.find("[id$=StartPositionescape]").parent().parent().show();
      table.find("[id$=EndPosition]").parent().parent().show();
      table.find("[id$=TopBottomend]").parent().parent().show();
      table.find("[id$=EndPositionSubcategory]").parent().parent().show();
    }
    else if( $(this).val() == "Retention"){
      table.find("[id$=EndPosition]").parent().parent().hide();
      table.find("[id$=TopBottomend]").parent().parent().hide();
      table.find("[id$=EndSubmission]").parent().parent().hide();
      table.find("[id$=EndPositionSubcategory]").parent().parent().hide();
      table.find("[id$=StartPositionescape]").parent().parent().hide();
      table.find("[id$=EndPosition]").val("");
      table.find("[id$=TopBottomend]").val("");
      table.find("[id$=EndSubmission]").val("");
      table.find("[id$=EndPositionSubcategory]").val("");
      table.find("[id$=StartPositionescape]").val("");
      table.find("[id$=StartPosition]").parent().parent().show();
      table.find("[id$=TopBottomstart]").parent().parent().show();
      table.find("[id$=StartPositionSubcategory]").parent().parent().show();
    }
    else if( $(this).val() == "Transition"){
      table.find("[id$=StartPositionescape]").parent().parent().hide();
      table.find("[id$=StartPositionescape]").val("");
      table.find("[id$=StartPosition]").parent().parent().show();
      table.find("[id$=TopBottomstart]").parent().parent().show();
      table.find("[id$=EndSubmission]").parent().parent().show();
      table.find("[id$=EndPosition]").parent().parent().show();
      table.find("[id$=TopBottomend]").parent().parent().show();
      table.find("[id$=StartPositionSubcategory]").parent().parent().show();
    }
  });
  $("[id$=EndSubmission]")
  .change(function (){
  table = $(this).parent().parent().parent();
    if( $(this).val() != "" ){
      table.find("[id$=EndPosition]").parent().parent().hide();
      table.find("[id$=TopBottomend]").parent().parent().hide();
      table.find("[id$=EndPosition]").val("");
      table.find("[id$=TopBottomend]").val("");
    }
    else {
      table.find("[id$=EndPosition]").parent().parent().show();
      table.find("[id$=TopBottomend]").parent().parent().show();
    }
  })
  $("[id$=EndPosition]")
  .change(function (){
    table = $(this).parent().parent().parent();
    if( $(this).val() != "" ){
      table.find("[id$=EndSubmission]").parent().parent().hide();
      table.find("[id$=EndSubmission]").val("");
    }
    else {
      table.find("[id$=TopBottomend]").val("");
      table.find("[id$=EndSubmission]").parent().parent().show();
    }
  })
}
function sessionEvaluationConstrains(){
  $("#id_SessionEvaluation-Injury").change(function (){
    if( $("#id_SessionEvaluation-Injury:checked").length > 0 ){
      $("#id_SessionEvaluation-injurySeverity").parent().parent().show()
      $("#id_SessionEvaluation-NoteOnInjury").parent().parent().show();
    }
    else{
      $("#id_SessionEvaluation-injurySeverity").parent().parent().hide()
      $("#id_SessionEvaluation-NoteOnInjury").parent().parent().hide();
    }
  })
}

function addForm(){
  disposableNode = node.code.cloneNode(true);
  forms = document.querySelectorAll('form table tbody');
  newForm = $(disposableNode).html().replace(/-\d-/g,'-'+forms.length+'-');
  newFormContainer = $("<tbody></tbody>").append(newForm);
  $('form table tbody').last().after(newFormContainer);
  $("[id$='TOTAL_FORMS']")[0].value = forms.length+1;
  $('tbody').addClass("border");
  techniqueConstrains()
  bindOptionConstrains(forms.length)
}

function filterSelectOptions(selectElement, attributeName, attributeValue) {
    if (selectElement.data("currentFilter") != attributeValue) {
        selectElement.data("currentFilter", attributeValue);
        var originalHTML = selectElement.data("originalHTML");
        if (originalHTML)
            selectElement.html(originalHTML)
        else {
            var clone = selectElement.clone();
            clone.children("option[selected]").removeAttr("selected");
            selectElement.data("originalHTML", clone.html());
        }
        if (attributeValue) {
            selectElement.children("option:not([" + attributeName + "='" + attributeValue + "'],:not([" + attributeName + "]))").remove();
        }
    }
}
