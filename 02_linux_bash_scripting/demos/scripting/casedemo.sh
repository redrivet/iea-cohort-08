read thing

case $thing in
     a*b) echo 'a*b';;
     ???) echo '3 letters';;
    *foo) echo 'ends in foo';;
 [aeiou]) echo 'single vowel';;
       *) echo 'something else';;
esac
