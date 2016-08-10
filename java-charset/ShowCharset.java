// ShowCharset.java: print the java default charset.
// Thanks to Roedy Green, https://groups.google.com/forum/#!msg/comp.lang.java.help/hKbaojrSb6E/DJhmo7bpaXUJ

import java.nio.charset.Charset;

class ShowCharset {
  public static void main(String[] args) {
    String defaultEncoding = System.getProperty( "file.encoding" );
    String canonicalName = Charset.forName( defaultEncoding ).name();
    System.out.println(canonicalName);
  } //main
};

// vi: set ts=2 sts=2 sw=2 et ai: //

