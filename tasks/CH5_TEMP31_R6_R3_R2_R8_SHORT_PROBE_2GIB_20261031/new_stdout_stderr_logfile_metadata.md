# R8 new owned logs: identities only

{
  "native_stdout.txt": {
    "bytes": 43,
    "sha256": "7a78231ca43e77a61b26e7b28a2deb9a07415344f3214e20bcf2ff1adf263ed4",
    "git_blob": "95c36bdd64c6514663a3ed34233f3b2db74bbae2"
  },
  "native_stderr.txt": {
    "bytes": 0,
    "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "git_blob": "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"
  },
  "native_matlab.log": {
    "bytes": 42,
    "sha256": "a915dab1e62dcf78403ed92552cf6b9a1e7b792ae703d36d0853741eb14b3e83",
    "git_blob": "448065f7acf6a413399bcfce8c9afdeac7d676af"
  }
}

All3 files actually exist, including the0-byte native stderr. No raw stdout/stderr/logfile or preference content is published. Native stdio was captured by the owned CreateFileW handles; isolated logfile was supplied in the checked argv. Markers and natural exit0 independently establish the minimal probe outcome. Raw run logs and marker nonce remain LOCAL_ONLY. Outer entry presentation capture is PowerShell-decoded text, not falsely described as the original native bytes. Historical logs were not read.
