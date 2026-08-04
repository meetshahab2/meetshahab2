// mobile nav toggle
    var toggle = document.getElementById('navToggle');
    var links = document.getElementById('navLinks');
    if(toggle){
        toggle.addEventListener('click', function(){
            var open = links.classList.toggle('open');
            toggle.setAttribute('aria-expanded', open);
        });
    }

    // scroll reveal
    if('IntersectionObserver' in window){
        var io = new IntersectionObserver(function(entries){
            entries.forEach(function(e){
                if(e.isIntersecting){
                    e.target.classList.add('in');
                    io.unobserve(e.target);
                }
            });
        }, {threshold:.15});

        document.querySelectorAll('.reveal').forEach(function(el){ io.observe(el); });
    } else {
        document.querySelectorAll('.reveal').forEach(function(el){ el.classList.add('in'); });
    }
