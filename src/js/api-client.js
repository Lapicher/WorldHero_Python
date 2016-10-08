var $=require('jquery');

module.exports={
    save: function(comment, successCallback, errorCallback){
      $.ajax({
          url: "/api/comments/",
          method: "post",
          data: comment,
          success: successCallback,
          error: errorCallback
      });
    },
    list: function(successCallback, errorCallback){
      $.ajax({
          url: "/api/comments/?_order=fecha",
          method: "get",
          success: successCallback,
          error: errorCallback
      });
    }
};
