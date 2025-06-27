"use strict";
// Global variables for our save game data object and a few other key things.
var save_data = new Object();
var mime_type = "";
var file_name = "";
var compressed = true;
var faction_id = "";
var playing_servants = false;
var alien_id = "";

// Special case non function code to allow the file upload button to work.
document.addEventListener("DOMContentLoaded", function() {
    var fileSelector = document.getElementById("file_selector");
    fileSelector.addEventListener("change", (event) => {
        var fileList = event.target.files;
        import_save_file(fileList[0])
    });
}, false);

function import_save_file(file){
    // If the filename already has an "_edited" tag then remove it so we don't end up adding more and more of them.
    var chopped_file_name = file.name.replace("_edited", "");
    // Get the file extension.
    var file_name_parts = chopped_file_name.split(".");
    var file_extension = file_name_parts[file_name_parts.length - 1];
    // Set a new filename for the modified save so users don't automatically overwrite their unmodified save files.
    file_name = file_name_parts[0] + "_edited." + file_name_parts[file_name_parts.length - 1];
    
    var reader = new FileReader();
    reader.addEventListener("load", (event) => {
        if (file_extension == "gz") {
            // If the save is compressed then split the actual file data off from the browser added MIME type tag.
            var file = event.target.result.split(",");
            // Set the mime type for when we export a file back to the user later.
            mime_type = "application/octet-stream";
            // Then decompress the save data.
            unzip(file[1]);
        }
        else {
            // If the save is not compressed then set a mime type for later and load the save as a JSON object directly.
            mime_type = "application/json";
            // Hack to fix incorrect JSON edge case.
            var fixed_save = event.target.result.replaceAll("Infinity,", "\"Infinity\",");
            save_data = JSON.parse(fixed_save);
            // Then start updating the UI with information from the save.
            find_faction();
        };
    });
    // Read compresed save files as binary data.
    if (file_extension == "gz") {
        reader.readAsDataURL(file);
    }
    // Read uncompressed save files as plain text.
    else {
        reader.readAsText(file);
        compressed = false;
    };
};

function find_faction(){
    // Work out what faction the player is, store the faction ID for later use, get their alien hate level, and display the faction logo in the UI.
    var faction_ids = Object.keys(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIPlayerState"])
    
    for (var i = 0; i < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIPlayerState"].length; i++){
        if (save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIPlayerState"][faction_ids[i]]["Value"]["isAI"] == false){
            faction_id = get_faction_id_from_player_id(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIPlayerState"][faction_ids[i]]["Value"]["ID"]["value"]);
            var faction_name = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIPlayerState"][faction_ids[i]]["Value"]["name"];
        };
        if (save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIPlayerState"][faction_ids[i]]["Value"]["name"] == "AlienPlayer" && faction_name != "SubmitPlayer"){
            alien_id = get_faction_id_from_player_id(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIPlayerState"][faction_ids[i]]["Value"]["ID"]["value"]);
            for (var i = 0; i < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"].length; i++){
                if(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Key"]["value"] == alien_id){
                    for (var x = 0; x < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["factionHate"].length; x++){
                        if (save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["factionHate"][x]["Key"]["value"] == faction_id){
                            document.getElementById("hate").value = Math.round(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["factionHate"][x]["Value"]);
                            break;
                        };
                    };
                };
            };
        };
    };    
    if (faction_name == "ResistPlayer"){
        document.getElementById("faction_logo").innerHTML = "<img src='images/resistance.png' alt='The Resistance'>";
    }
    else if (faction_name == "DestroyPlayer"){
        document.getElementById("faction_logo").innerHTML = "<img src='images/humanity.png' alt='Humanity First'>";
    }
    else if (faction_name == "ExploitPlayer"){
        document.getElementById("faction_logo").innerHTML = "<img src='images/initiative.png' alt='The Initiative'>";
    }
    else if (faction_name == "SubmitPlayer"){
        document.getElementById("faction_logo").innerHTML = "<img src='images/servants.png' alt='The Servants'>";
        playing_servants = true;
    }
    else if (faction_name == "AppeasePlayer"){
        document.getElementById("faction_logo").innerHTML = "<img src='images/protectorate.png' alt='The Protectorate'>";
    }
    else if (faction_name == "CooperatePlayer"){
        document.getElementById("faction_logo").innerHTML = "<img src='images/academy.png' alt='The Academy'>";
    }
    else if (faction_name == "EscapePlayer"){
        document.getElementById("faction_logo").innerHTML = "<img src='images/exodus.png' alt='Project Exodus'>";
    }
    // Display the number of loose nukes.
    document.getElementById("nukes").value = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIGlobalValuesState"][0]["Value"]["looseNukes"];
    // Then move on to displaying faction resources in the UI.
    display_resources();
};

function input_check(event){
    // Input sanitization. Only allow numbers.
    var theEvent = event || window.event;
    if (theEvent.type === "paste") {
        key = event.clipboardData.getData("text/plain");
    }
    else {
        var key = theEvent.keyCode || theEvent.which;
        key = String.fromCharCode(key);
    };
    var regex = /[0-9]|\./;
    if(!regex.test(key)){
        theEvent.returnValue = false;
        if(theEvent.preventDefault) {
            theEvent.preventDefault();
        };
        return false;
    };
    return true;
};

function update_resource(){
    if (file_name == "") {
        // Don't do anything if the user hasn't uploaded a saved game yet.
        return false;
    };
    // Update the save game data with the new values entered by the user.
    for (var i = 0; i < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"].length; i++){
        if (save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Key"]["value"] == faction_id){
            save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Money"] = parseInt(document.getElementById("funding").value);
            save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Influence"] = parseInt(document.getElementById("influence").value);
            save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Operations"] = parseInt(document.getElementById("ops").value);
            save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Boost"] = parseInt(document.getElementById("boost").value);
            save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Water"] = parseInt(document.getElementById("water").value);
            save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Volatiles"] = parseInt(document.getElementById("volatiles").value);
            save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Metals"] = parseInt(document.getElementById("metal").value);
            save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["NobleMetals"] = parseInt(document.getElementById("nobles").value);
            save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Fissiles"] = parseInt(document.getElementById("fissiles").value);
            save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Exotics"] = parseInt(document.getElementById("exotics").value);
            save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Antimatter"] = parseInt(document.getElementById("antimatter").value);
            break;
        };
    };
};

function display_resources(){
    // Read the resource totals from the save data and display them in the UI.
    for (var i = 0; i < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"].length; i++){
        if (save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Key"]["value"] == faction_id){
            document.getElementById("funding").value = Math.round(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Money"]);
            document.getElementById("influence").value = Math.round(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Influence"]);
            document.getElementById("ops").value = Math.round(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Operations"]);
            document.getElementById("boost").value = Math.round(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Boost"]);
            document.getElementById("water").value = Math.round(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Water"]);
            document.getElementById("volatiles").value = Math.round(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Volatiles"]);
            document.getElementById("metal").value = Math.round(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Metals"]);
            document.getElementById("nobles").value = Math.round(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["NobleMetals"]);
            document.getElementById("fissiles").value = Math.round(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Fissiles"]);
            document.getElementById("exotics").value = Math.round(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Exotics"]);
            document.getElementById("antimatter").value = Math.round(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["resources"]["Antimatter"]);
            break;
        };
    };
    // Then move on to displaying councilor stats in the UI.
    display_councilors();
};

function display_councilors(){
    var slot = 1;
    for (var i = 0; i < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"].length; i++){
        try {
            if (save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["faction"]["value"] == faction_id){
                var tab_name = "councilor" + slot + "-tab";
                var first_name = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["personalName"];
                var last_name = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["familyName"];
                document.getElementById(tab_name).innerHTML = first_name + " " + last_name;
                document.getElementById("persuasion" + slot).value = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["attributes"]["Persuasion"];
                document.getElementById("investigation" + slot).value = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["attributes"]["Investigation"];
                document.getElementById("espionage" + slot).value = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["attributes"]["Espionage"];
                document.getElementById("command" + slot).value = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["attributes"]["Command"];
                document.getElementById("administration" + slot).value = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["attributes"]["Administration"];
                document.getElementById("science" + slot).value = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["attributes"]["Science"];
                document.getElementById("security" + slot).value = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["attributes"]["Security"];
                document.getElementById("loyalty" + slot).value = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["attributes"]["Loyalty"];
                var birthday = make_date_object(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["dateBorn"]);
                var current_date = make_date_object(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TITimeState"][0]["Value"]["currentDateTime"]);
                var age_delta = Math.abs(current_date - birthday);
                document.getElementById("age" + slot).value = Math.round(age_delta / 31536000000);
                document.getElementById("class" + slot).value = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["typeTemplateName"];
                for (var x = 0; x < traits.length; x++){
                    if(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["traitTemplateNames"].includes(traits[x])){
                        document.getElementById("active" + slot).add(new Option(traits[x]));
                    }
                    else {
                        document.getElementById("available" + slot).add(new Option(traits[x]));
                    };
                };
                slot = slot + 1;
            };
        }
        catch {
            // Do nothing. This is just here because councilors that haven't been hired have a null for their faction ID value and Javascript's == operator doesn't like that.
        };
    };
    // Then display the research.
    display_research();
};

function display_research(){
    var slot = 1;
    for (var i = 0; i < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIGlobalResearchState"][0]["Value"]["techProgress"].length; i++){
        document.getElementById("global" + slot).innerHTML = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIGlobalResearchState"][0]["Value"]["techProgress"][i]["techTemplateName"];
        document.getElementById("globalr" + slot).value = Math.round(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIGlobalResearchState"][0]["Value"]["techProgress"][i]["accumulatedResearch"]);
        slot = slot + 1;
    };
    for (var i = 0; i < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"].length; i++){
        if (save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Key"]["value"] == faction_id){
            for(var q = 0; q < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["currentProjectProgress"].length; q++){
                if(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["currentProjectProgress"][q]["slot"] == 3){
                    var project_parts = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["currentProjectProgress"][q]["projectTemplateName"].split("_");
                    document.getElementById("project1").innerHTML = project_parts[1];
                    document.getElementById("projectr1").value = Math.round(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["currentProjectProgress"][q]["accumulatedResearch"]);
                };
                if(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["currentProjectProgress"][q]["slot"] == 4){
                    var project_parts = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["currentProjectProgress"][q]["projectTemplateName"].split("_");
                    document.getElementById("project2").innerHTML = project_parts[1];
                    document.getElementById("projectr2").value = Math.round(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["currentProjectProgress"][q]["accumulatedResearch"]);
                };
                if(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["currentProjectProgress"][q]["slot"] == 5){
                    var project_parts = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["currentProjectProgress"][q]["projectTemplateName"].split("_");
                    document.getElementById("project3").innerHTML = project_parts[1];
                    document.getElementById("projectr3").value = Math.round(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["currentProjectProgress"][q]["accumulatedResearch"]);
                };
            };
            break;
        };
    };
};

function update_project_research(){
    if (file_name == "") {
        // Don't do anything if the user hasn't uploaded a saved game yet.
        return false;
    };
    for (var i = 0; i < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"].length; i++){
        if (save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Key"]["value"] == faction_id){
            for(var q = 0; q < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["currentProjectProgress"].length; q++){
                if(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["currentProjectProgress"][q]["slot"] == 3){
                    save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["currentProjectProgress"][q]["accumulatedResearch"] = parseInt(document.getElementById("projectr1").value);
                };
                if(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["currentProjectProgress"][q]["slot"] == 4){
                    save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["currentProjectProgress"][q]["accumulatedResearch"] = parseInt(document.getElementById("projectr2").value);
                };
                if(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["currentProjectProgress"][q]["slot"] == 5){
                    save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["currentProjectProgress"][q]["accumulatedResearch"] = parseInt(document.getElementById("projectr3").value);
                };
            };
            break;
        };
    };
};

function update_global_research(){
    if (file_name == "") {
        // Don't do anything if the user hasn't uploaded a saved game yet.
        return false;
    };
    var slot = 1;
    for (var i = 0; i < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIGlobalResearchState"][0]["Value"]["techProgress"].length; i++){
        save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIGlobalResearchState"][0]["Value"]["techProgress"][i]["accumulatedResearch"] = parseInt(document.getElementById("globalr" + slot).value);
        slot = slot + 1;
    };
};

function make_date_object(ti_date){
     var converted_date = new Date(ti_date["year"] + "-" + ti_date["month"] + "-" + ti_date["day"]);
     return converted_date;
};

function update_stats(){
    if (file_name == "") {
        // Don't do anything if the user hasn't uploaded a saved game yet.
        return false;
    };
    if (parseInt(document.getElementById("age" + slot).value) < 18){
        document.getElementById("age" + slot).value = "18";
    };
    var slot = 1;
    for (var i = 0; i < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"].length; i++){
        try {
            if (save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["faction"]["value"] == faction_id){
                save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["attributes"]["Persuasion"] = parseInt(document.getElementById("persuasion" + slot).value);
                save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["attributes"]["Investigation"] = parseInt(document.getElementById("investigation" + slot).value);
                save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["attributes"]["Espionage"] = parseInt(document.getElementById("espionage" + slot).value);
                save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["attributes"]["Command"] = parseInt(document.getElementById("command" + slot).value);
                save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["attributes"]["Administration"] = parseInt(document.getElementById("administration" + slot).value);
                save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["attributes"]["Science"] = parseInt(document.getElementById("science" + slot).value);
                save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["attributes"]["Security"] = parseInt(document.getElementById("security" + slot).value);
                save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["attributes"]["Loyalty"] = parseInt(document.getElementById("loyalty" + slot).value);
                var current_date = make_date_object(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TITimeState"][0]["Value"]["currentDateTime"]);
                var new_birth_year = Math.abs(current_date - (parseInt(document.getElementById("age" + slot).value) * 31536000000));
                save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["dateBorn"]["year"] = new_birth_year.getFullYear();
                save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["typeTemplateName"] = parseInt(document.getElementById("class" + slot).value);
                slot = slot + 1;
            };
        }
        catch {
            // Do nothing. This is just here because councilors that haven't been hired have a null for their faction ID value and Javascript's == operator doesn't like that.
        };
    };
};

function remove_trait(slot){
    if (file_name == "") {
        // Don't do anything if the user hasn't uploaded a saved game yet.
        return;
    };
    var element = document.getElementById("active" + slot);
    var iteration = 1;
    for (var i = 0; i < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"].length; i++){
        try {
            if (save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["faction"]["value"] == faction_id){
                if (iteration == parseInt(slot)){
                    var index = save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["traitTemplateNames"].indexOf(element.value);
                    save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["traitTemplateNames"].splice(index, 1);
                    break;
                };
                iteration = iteration + 1;
            };
        }
        catch {
            // Do nothing. This is just here because councilors that haven't been hired have a null for their faction ID value and Javascript's == operator doesn't like that.
        };
    };
    document.getElementById("available" + slot).add(new Option(element.value));
    element.remove(element.selectedIndex);
};

function add_trait(slot){
    if (file_name == "") {
        // Don't do anything if the user hasn't uploaded a saved game yet.
        return;
    };
    var element = document.getElementById("available" + slot);
    var iteration = 1;
    for (var i = 0; i < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"].length; i++){
        try {
            if (save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["faction"]["value"] == faction_id){
                if (iteration == parseInt(slot)){
                    save_data["gamestates"]["PavonisInteractive.TerraInvicta.TICouncilorState"][i]["Value"]["traitTemplateNames"].push(element.value);
                    break;
                };
                iteration = iteration + 1;
            };
        }
        catch {
            // Do nothing. This is just here because councilors that haven't been hired have a null for their faction ID value and Javascript's == operator doesn't like that.
        };
    };
    document.getElementById("active" + slot).add(new Option(element.value));
    element.remove(element.selectedIndex);
};

function update_hate(){
    if (file_name == "") {
        // Don't do anything if the user hasn't uploaded a saved game yet.
        return false;
    };
    // Don't try to set an alien hate level for the Servants faction.
    if (playing_servants) {
        return;
    };
    for (var i = 0; i < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"].length; i++){
        if(save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Key"]["value"] == alien_id){
            for (var x = 0; x < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["factionHate"].length; x++){
                if (save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["factionHate"][x]["Key"]["value"] == faction_id){
                    save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["factionHate"][x]["Value"] = parseInt(document.getElementById("hate").value);
                    break;
                };
            };
        };
    };
};

function update_nukes(){
    if (file_name == "") {
        // Don't do anything if the user hasn't uploaded a saved game yet.
        return false;
    };
    save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIGlobalValuesState"][0]["Value"]["looseNukes"] = parseInt(document.getElementById("nukes").value);
};

function get_faction_id_from_player_id(player_id){
    for (var i = 0; i < save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"].length; i++){
        if (save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Value"]["player"]["value"] == player_id) {
           return save_data["gamestates"]["PavonisInteractive.TerraInvicta.TIFactionState"][i]["Key"]["value"];
        };
    };
};

function export_to_file(){
    if (file_name == "") {
        // Don't do anything if the user hasn't uploaded a saved game yet.
        return;
    };
    // Convert our JSON object to a string with pretty whitespace.
    var saved_game = JSON.stringify(save_data, null, 4);
    // Revert our incorrect JSON edge case fix.
    saved_game = saved_game.replaceAll("v\"Infinity\",", "Infinity,");
    // If the user gave us a compressed save file then we need to compress the save data before giving it back to them.
    if (compressed) {
        saved_game = pako.gzip(saved_game);
    };
    // Then ask the browser to download the file.
    try {
        var b = new Blob([saved_game],{type:mime_type});
        saveAs(b, file_name);
    }
    catch (e) {
        window.open("data:"+mime_type+"," + encodeURIComponent(saved_game), "_blank", "");
    };
};

function unzip(compressed_data){
    // Process the base64 encoded binary data into the format pako expects.
    var str_data = atob(compressed_data);
    var char_data = str_data.split("").map(function(x){return x.charCodeAt(0);});
    var processed_data = new Uint8Array(char_data);
    // Then decompress it.
    var raw_save_data = pako.inflate(processed_data, { to: "string" });
    // Hack to fix incorrect JSON edge case.
    var fixed_save = raw_save_data.replaceAll("Infinity,", "\"Infinity\",");
    // Load the data as a JSON object.
    save_data = JSON.parse(fixed_save);
    // Then start updating the UI with information from the save.
    find_faction();
};
