 const mntoggle = document.querySelector('.menu-toggle input');
 const nav = document.querySelector('nav ul');

mntoggle.addEventListener('click',function(){
    nav.classList.toggle('menushow');

    $(function(){
        $.get(.../pertemuan_8/headline.json, function(obj){
            var headline=obj.split(`\n`);
            var str=``;

            for (var i=0; i<headline.length; i++){
                str+=${headline[i]}+'</br>';
            }
            $('#headline').html(str);
    })
})
})