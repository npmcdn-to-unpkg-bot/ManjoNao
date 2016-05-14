
angular.module('manjoAPP',[], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

angular.module('manjoAPP').controller('manjoCtrl',function ($scope, $http){
	$scope.myPosts = [];

	$scope.updatethat = false;

	var carregarDados = function(){
		$http.get('backcall/getAll').success(function (data,status){
			$scope.myPosts = data;
			console.log(data);
		}).error(function (data) {
			console.log('Deu ruim');
		});

	};

	$scope.submitThat = function (post){
		console.log(post);
		$http.post('backcall/saveThat/insert',post).success(function(data){
			delete $scope.post;
			carregarDados();
			$scope.manjoForm.$setPristine();
				
		});
	};

	
	$scope.update_that = function (post){
		$http.post('backcall/saveThat/update',post).success(function(data){
			delete $scope.post;
			carregarDados();
			$scope.manjoForm.$setPristine();
				
		});	
	};

	$scope.apagar_this = function(myPosts){
		$scope.myPosts = myPosts.filter(function(post){
			if (!post.selecionado) return post;
		});
		
	};

	$scope.apagar_one = function(id){
		var delete_this = $scope.myPosts[id];
		$scope.myPosts.splice(delete_this,1);
		$http.delete('backcall/delThat',{params: {id:delete_this.id} }).success(function(data){
			carregarDados();
		});
		
	};

	$scope.edit_that = function(post){
		$scope.updatethat = true;
		$scope.current = post;
		$scope.post = $scope.myPosts[post];
	};
	carregarDados();
	console.log($scope.updatethat);
});


function chances(what){
	if (what == 'about'){
		$("#conteiner").css('margin-top','80px');
		$("#manja").hide();
		$("#about").show();

	}
	if (what == 'manja'){
		$("#conteiner").css('margin-top','20px');
		$("#about").hide();
		$("#manja").show();

	}
}