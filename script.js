document.addEventListener('DOMContentLoaded', function () {
    // element-one: Hozzáad egy "box1style" class-t kattintáskor
    const elementOne = document.getElementById('element-one');
    document.getElementById('element-one').onclick=function(){
        document.getElementById('element-one').classList.add("box1style")
    }

    // element-two: Dupla kattintásra hozzáad egy 2px-es, fekete keretet
    const elementTwo = document.getElementById('element-two');
    document.getElementById('element-two').ondblclick=function(){
        document.getElementById('element-two').style.border='solid'
    }


    // element-three: Ha rámegy az egér, eltűnik
    const elementThree = document.getElementById('element-three');
    document.getElementById('element-three').onmouseover=function(){
        document.getElementById('element-three').style.opacity=0
    }


    // element-four: Kattintásra a szövegszín piros lesz benne
    const elementFour = document.getElementById('element-four');
    document.getElementById('element-four').onclick=function(){
        document.getElementById('element-four').style.color='red'
    }
    
    


    // Input mező: Billentyű lenyomásra az inputmező háttérszíne szürke lesz
    const inputField = document.getElementById('myInput');
    
    
});