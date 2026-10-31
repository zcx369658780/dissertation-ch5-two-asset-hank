# New run logs retained LOCAL_ONLY

{
  "native_stdout.txt": {
    "bytes": 228,
    "sha256": "e474ecfa637b04a7f36022d0502bc27a6b0f3f968f4e93e5dba1e5f95ae67406",
    "git_blob": "cde8609fdd197c99a84e84581566b66c951e367f"
  },
  "native_stderr.txt": {
    "bytes": 176,
    "sha256": "f187c035db585c5ad4ea933d122185e28d30f0ed54bc7e88e2878793bb42e382",
    "git_blob": "a8310b39fd4c1c436393368dd3bb26a27d509352"
  },
  "native_matlab.log": {
    "bytes": 439,
    "sha256": "dbd2e048c6a8d5c0e179af4b7e194190a4cab2925a917e541d60f6e3df818094",
    "git_blob": "4895068d450a06abe92d1c648daadf30028e0c08"
  }
}

Stdout/stderr strictly decode as gb18030; isolated logfile strictly decodes as UTF8. Original bytes are unmodified; decoded content and private paths stay LOCAL_ONLY. Public compatibility evidence replaces the probe name and its63-character prefix by roles and removes display control backspaces. The logfile directly warns of65-versus63 character truncation and reports an unrecognized truncated name in run/evalin. No first marker exists. Log text does not authenticate runtime release or prove the historical1GiB resource cause. No historical native log was opened.
