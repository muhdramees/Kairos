
$(document).ready(function(){
    
    $('.increment-btn').click(function (e){
        e.preventDefault();
        console.log('clicked@')
        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(inc_value,10); 
        value = isNaN(value) ? 0 : value;
        if(value < 15)
        {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
        
    });

    $('.decrement-btn').click(function (e){
        e.preventDefault();

        var dec_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(dec_value,10); 
        value = isNaN(value) ? 0 : value;
        if(value > 1)
        {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.addtocartbtn').click(function(e){
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        
        $.ajax({
            method:"POST",
            url:"/add-to-cart/",
            data:{
                'product_id':product_id,
                'product_qty':product_qty,
                'csrfmiddlewaretoken': token
            },
          
            success: function(response){
                console.log(response)
                alertify.success(response.status)

            }

        });
    });



    $('.addToWishlist').click(function (e) {
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken').val();


        $.ajax({
            method:"POST",
            url:"/add-to-wishlist/",
            data:{
                'product_id':product_id,
                'csrfmiddlewaretoken' :token
            },
            success:function(response){
                console.log(response)
                alertify.success(response.status)

            }
            
        });
    });



    $('.changeQuantity').click(function(e){
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        
        $.ajax({
            method:"POST",
            url:"/update-cart/",
            data:{
                'product_id':product_id,
                'product_qty':product_qty,
                'csrfmiddlewaretoken': token
            },
          
            success: function(response){
                console.log("sdftg")
                console.log(response.status)
                
                alertify.success(response.status)
                location.reload();
           


            }

        });
    });

    $('.delete-cart-item').click(function (e){
        e.preventDefault();
        
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url:"/delete-cart-item/",
            data:{
                'product_id':product_id,
                'csrfmiddlewaretoken':token
            },
            success: function (response){
                console.log(response)
                alertify.success(response.status)
                $('.cartdata').load(location.href +  " .cartdata");


               

            }
            
        });
    });


    $('.delete-wishlist-item').click(function (e){
        e.preventDefault();
        
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url:"/delete-wishlist-item/",
            data:{
                'product_id':product_id,
                'csrfmiddlewaretoken':token
            },
            success: function (response){
                alertify.success(response.status)
                location.reload();

            }
        });
    });




    $('.delete_category_offer').click(function (e){
        e.preventDefault();
        
        var cat_offer_id = $(this).closest('.category_offer_data').find('.cat_offer_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url:"/delete-category-offer/",
            data:{
                'cat_offer_id':cat_offer_id,
                'csrfmiddlewaretoken':token
            },
            success: function (response){
                alertify.success(response.status)
                $('.cartdata').load(location.href + ".cartdata")

            }
        });
    });



   
    

});


