$(document).ready(function(){

    $('.payWithRazorpay').click(function (e) {
        e.preventDefault();
        console.log("RAzerpay")

    // $(document).on('click', '.payWithRazorpay', function (e) {
    //     e.preventDefault();
    //     console.log("Razorpay")

        var fname = $("[name ='fname']").val();
        var lname = $("[name='lname']").val();
        var email = $("[name='email']").val();
        var phone = $("[name='phone']").val();
        var address = $("[name='address']").val();
        var city = $("[name='city']").val();
        var state = $("[name='state']").val();
        var country = $("[name='country']").val();
        var pincode = $("[name='pincode']").val();
        var token = $("[name='csrfmiddlewaretoken']").val();

        if (fname == "" || lname == "" || email == "" || phone == "" || address == "" || city == "" || state == "" || country == "" || pincode == "")
        {
            swal({
                icon: "Alert",
              });
            console.log("eror");
            return false;
        }

        else
        {
            $.ajax({
                method: "GET",
                url: "/proceed-to-pay/",
                success: function (response) {
                    console.log(response);

                    var options = {
                        "key": "rzp_test_3lEvNyhWjrvwyH", // Enter the Key ID generated from the Dashboard
                        "amount": 1*100, //response.total_price*100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                            "currency": "INR",
                        "name": "Kairos", //your business name
                        "description": "Have a Good Day",
                        "image": "https://example.com/your_logo",
                        // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        // "callback_url": "https://eneqd3r9zrjok.x.pipedream.net/",

                        "handler": function (responseb){
                            alert(responseb.razorpay_payment_id);
                            data = {
                                "fname" : fname,
                                "lname" : lname,
                                "email" : email,
                                "phone" : phone,
                                "address" : address,
                                "city" : city,
                                "state" : state,
                                "country" : country,
                                "pincode" : pincode,
                                "payment_mode" : "Paid by Razorpay",
                                "payment_id" : responseb.razorpay_payment_id,
                                csrfmiddlewaretoken : token
                                
                            }
                            $.ajax({
                                method: "POST",
                                url: "/placeorder/",
                                data: data,
                        
                                success: function (responsec){
                                    swal("Congratulations!", responsec.status, "success").then((value) => {
                                        window.location.href = '/my-order/'
                                    });


                                }
                            });
                        },

                        "prefill": {
                            "name": fname+" "+lname,
                            "email": email,
                            "contact": phone
                        },
                       
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
            
                    var rzp1 = new Razorpay(options);
                    rzp1.open();

                }
            })

            
        }
        
    });
})