function JeuMemoire(options) {
        this._defaultOptions = {
            tableauCartes: [1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12], 
            peutCliquer: false,
            nbCartesRestantes: 0,
            contenantGrille: "",
            bouton: ""
        };
        this._options = $.extend({}, this._defaultOptions, options || {});
        this._grille;
        this._bouton;
        this._cartes = {
            premiere: null,
            deuxieme: null
        }
        this._init();
}

JeuMemoire.prototype = {
    _init: function() {
        var _self = this;
        
        this._bouton = $("#" + this._options.bouton).button();
        this._bouton.on('click', this._nouvellePartie);
        
        this._grille = $('#' + this._options.contenantGrille).grid('option', 'cellChangeFlippedState', function(e, info) {
            return _self._traiterFlip(e, info, _self);
        });
    },
    
    _nouvellePartie: function() {
        nouvellePartie();
    },
    
    _resetCartes: function() {
        this._cartes.premiere = null;
        this._cartes.deuxieme = null;
    },
    
    _cacherCartes: function() {
        this._grille
            .grid('cellsFlipped')
                .cell('option', 'flipped', false);

        this._resetCartes();
    },
    
    _enleverCartes: function() {
        this._grille
            .grid('cellsFlipped')
                .cell('clear')
                .cell('option', 'disabled', true);
                
        this._options.nbCartesRestantes -= 2;
                
        this._resetCartes();
    },
    
    _afficherFinPartie: function() {
        var _self = this;
        
        this._grille
            .grid('cells')
                .each(function(index) {
                    $(this).cell('option', {
                        'image': "image" + _self._options.tableauCartes[index] + ".png"
                    });
                });    
    },
    
    _traiterFlip: function(e, info, me) {
        if(info.newOptions.flipped) {
            if(me._options.peutCliquer) {
                if(me._cartes.premiere) {
                    me._options.peutCliquer = false;
                    me._cartes.deuxieme = info.cellElement;
                    traiterCartes();
                } else {
                    me._cartes.premiere = info.cellElement;
                }
            }
            else {
                return false;
            }
        } else {
            if(me._options.peutCliquer) {
                return false;
            }
        }
    },
    
    set: function(key, value) {
        this._options[key] = value;
    },
    
    melangerCartes: function() {
        for(var i = 0; i < this._options.tableauCartes.length * 2; i++)
        {
            var idx1 = this._options.tableauCartes.randomIndex(),
                idx2 = this._options.tableauCartes.randomIndex(),
                temp;
            
            temp = this._options.tableauCartes[idx1];
            this._options.tableauCartes[idx1] = this._options.tableauCartes[idx2];
            this._options.tableauCartes[idx2] = temp;
        }
    },
    
    initialiser: function() {
        var _self = this;
        
        this._grille
            .grid('cells')
                .each(function(index) {
                    $(this).cell('option', {
                        'disabled': false,
                        'image': "back.png",
                        'backImage': "image" + _self._options.tableauCartes[index] + ".png",
                        value: _self._options.tableauCartes[index]
                    });
                });    
                
		this._options.nbCartesRestantes = 24;
        this._options.peutCliquer = true;
    },
    
    cacherCartes: function(callback) {
        var _self = this;
        
        setTimeout(
            function(){
                _self._cacherCartes();
                if(callback) {
                    callback();
                }
            }, 
            1500
        );
    },
    
    enleverCartes: function(callback) {
        var _self = this;
        
        setTimeout(
            function(){
                _self._enleverCartes();
                if(callback) {
                    callback();
                }
            }, 
            1500
        );
    },
    
    partieEstTerminee: function() {
        return this._options.nbCartesRestantes == 0;
    },
    
    afficherFinPartie: function(callback) {
        var _self = this;
        
        setTimeout(
            function(){
                _self._afficherFinPartie();
                if(callback) {
                    callback();
                }
            }, 
            1000
        );
    },
    
    cartesSontIdentiques: function() {
        return this._cartes.premiere.cell('option', 'value') == this._cartes.deuxieme.cell('option', 'value');
    }
};