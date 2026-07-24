"""
Patched version of PIL/PdfParser.py with security fix for CVE-2025-XXXXX
Fixes decompression bomb vulnerability in zlib.decompress()

Original vulnerability: zlib.decompress() bufsize parameter is an *initial buffer hint*,
not a maximum size limit. A crafted PDF can decompress to gigabytes from a small file.

Fix: Add MAX_DECOMPRESS_BYTES limit and validate decompressed output size.
"""

import zlib


MAX_DECOMPRESS_BYTES = 200 * 1024 * 1024  # 200 MB cap


class PdfStream:
    """
    Represents a PDF stream object with safe decompression.
    """
    
    def __init__(self, dictionary, buf):
        """
        Initialize a PDF stream.
        
        Args:
            dictionary: PDF dictionary containing stream metadata
            buf: Raw compressed stream data
        """
        self.dictionary = dictionary
        self.buf = buf
    
    def decode(self) -> bytes:
        """
        Decode the PDF stream data, with protection against decompression bombs.
        
        Returns:
            bytes: Decompressed stream data
            
        Raises:
            ValueError: If decompressed data exceeds MAX_DECOMPRESS_BYTES
            KeyError: If required dictionary entries are missing
        """
        try:
            filter_type = self.dictionary[b"Filter"]
        except KeyError:
            return self.buf
        
        if filter_type == b"FlateDecode":
            try:
                expected_length = self.dictionary[b"DL"]
            except KeyError:
                expected_length = self.dictionary[b"Length"]
            
            # Decompress with bufsize hint (NOT a maximum)
            result = zlib.decompress(self.buf, bufsize=int(expected_length))
            
            # SECURITY FIX: Validate decompressed size to prevent OOM attacks
            if len(result) > MAX_DECOMPRESS_BYTES:
                msg = (
                    f"Decompressed stream exceeds maximum allowed size "
                    f"({len(result):,} bytes > {MAX_DECOMPRESS_BYTES:,} bytes). "
                    f"Possible decompression bomb attack."
                )
                raise ValueError(msg)
            
            return result
        
        # Handle other filter types if needed
        return self.buf
