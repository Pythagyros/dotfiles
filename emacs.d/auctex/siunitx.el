;;; siunitx.el --- AUCTeX style file for Siunitx
;;; Adapted from https://tex.stackexchange.com/questions/69031/auctex-style-for-siunitx

(TeX-add-style-hook "siunitx
	(function
		(lambda ()
		(TeX-add-symbols
		'("SI" "Value" "Unit")
		'("ang" "Angle")
	)))
)
		
	
