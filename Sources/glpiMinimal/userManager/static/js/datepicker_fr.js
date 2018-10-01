$(document).ready(
    function()
    {
	$('.datepicker').datepicker(
	    {
		firstDay: 1,
		format: 'yyyy-mm-dd',
		showClearBtn: 1,
		showDaysInNextAndPreviousMonths: 1,
		i18n:
		{
		    cancel: 'Annuler',
		    clear: 'Effacer',
		    done: 'Valider',
		    months: ['Janvier', 'Février', 'Mars',
			     'Avril', 'Mai', 'Juin',
			     'Juillet', 'Août', 'Septembre',
			     'Octobre', 'Novembre', 'Décembre'],
		    monthsShort: ['Janv.', 'Févr.', 'Mars', 'Avr.',
				  'Mai', 'Juin', 'Juill.', 'Août',
				  'Sept.', 'Oct.', 'Nov.', 'Déc.'],
		    weekdays: ['Lundi', 'Mardi', 'Mercredi', 'Jeudi',
			       'Vendredi', 'Samedi', 'Dimanche'],
		    weekdaysShort: ['Dim', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam'],
		    weekdaysAbbrev: ['D', 'L', 'M', 'M', 'J', 'V', 'S'],
		}
	    }
	);
    }
);
