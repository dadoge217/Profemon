function forfeit(profId){
    fetch('/forfeit/${profId}', {method: GET});
}