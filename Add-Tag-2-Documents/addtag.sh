# Add Tag in Documents Ordner
mkdir ~/Documents-Temp
rsync -a ~/Documents/ ~/Documents-Temp/
mkdir -m 0700 ~/D
echo "Please add a Tag to D in Finder. If you are ready with the Tag for D to continue, press ENTER"
say  "Please add a Tag to D in Finder. If you are ready with the Tag for D to continue, press ENTER"
read "ENTER"
chmod -N ~/Documents
rm -r ~/Documents 
mv -v ~/D ~/Documents
chmod +a "everyone deny delete" ~/Documents
killall Finder
rsync -a ~/Documents-Temp/  ~/Documents/
rm -r ~/Documents-Temp/ 
